from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages

import requests
import stripe
import uuid

from base import models as base_models
from doctor import models as doctor_models
from patient import models as patient_models

def index(request):
    services = base_models.Service.objects.all()
    context = {
        "services": services
    }
    return render(request, "base/index.html", context)

def service_detail(request, service_id):
    service = base_models.Service.objects.get(id=service_id)

    context = {
        "service": service
    }
    return render(request, "base/service_detail.html", context)

@login_required
def book_appointment(request, service_id, doctor_id):
    service = base_models.Service.objects.get(id=service_id)
    doctor = doctor_models.Doctor.objects.get(id=doctor_id)
    
    try:
        patient = patient_models.Patient.objects.get(user=request.user)
    except patient_models.Patient.DoesNotExist:
        messages.error(request, "Please complete your patient profile before booking an appointment")
        return redirect('/')  # Redirect to home page

    if request.method == "POST":
        # Process form data...
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        dob_value = request.POST.get("dob")
        issues = request.POST.get("issues")
        symptoms = request.POST.get("symptoms")

        # Update patient with form data
        patient.full_name = full_name
        patient.email = email
        patient.mobile = mobile
        patient.gender = gender
        patient.address = address
        
        # Only update DOB if provided
        if dob_value and dob_value.strip():
            patient.dob = dob_value
        
        patient.save()

        # Create appointment with correct field names
        appointment = base_models.Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            service=service,
            description=issues,  # Using correct field name
            notes=symptoms,      # Using correct field name
            status="Pending",
            appointment_id=str(uuid.uuid4()).split("-")[0]
        )

        messages.success(request, f"Appointment booked successfully: #{appointment.appointment_id}")
        
        # Redirect using namespaced URL name pattern
        return redirect('/patient/')  # Redirect to patient dashboard instead
        
    context = {
        "service": service,
        "doctor": doctor,
        "patient": patient
    }
    return render(request, "base/book_appointment.html", context)

@login_required
def checkout(request, billing_id):
    billing = base_models.Billing.objects.get(billing_id=billing_id)

    context = {
        "billing": billing,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "paypal_client_id": settings.PAYPAL_CLIENT_ID,
    }
    return render(request, "base/checkout.html", context)

@csrf_exempt
def stripe_payment(request, billing_id):
    billing = base_models.Billing.objects.get(billing_id=billing_id)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        customer_email=billing.patient.email,
        payment_method_types=['card'],
        line_items = [
            {
                'price_data': {
                    'currency': 'USD',
                    'product_data': {
                        'name': billing.patient.full_name
                    },
                    'unit_amount': int(billing.total * 100)
                },
                'quantity': 1
            }
        ],
        mode='payment',
        success_url = request.build_absolute_uri(reverse("base:stripe_payment_verify", args=[billing.billing_id])) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse("base:stripe_payment_verify", args=[billing.billing_id])) + "?session_id={CHECKOUT_SESSION_ID}"
        
    )
    return JsonResponse({"sessionId": checkout_session.id})


def stripe_payment_verify(request, billing_id):
    billing = base_models.Billing.objects.get(billing_id=billing_id)
    session_id = request.GET.get("session_id")
    session = stripe.checkout.Session.retrieve(session_id)

    if session.payment_status == "paid":
        if billing.status == "Unpaid":
            billing.status = "Paid"
            billing.save()
            billing.appointment.status = "Completed"
            billing.appointment.save()

            doctor_models.Notification.objects.create(
                doctor=billing.appointment.doctor,
                appointment=billing.appointment,
                type="New Appointment"
            )

            patient_models.Notification.objects.create(
                patient=billing.appointment.patient,
                appointment=billing.appointment,
                type="Appointment Scheduled"
            )

            return redirect(f"/payment_status/{billing.billing_id}/?payment_status=paid")
    else:
        return redirect(f"/payment_status/{billing.billing_id}/?payment_status=failed")
    

def get_paypal_access_token():
    token_url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
    data = {'grant_type': 'client_credentials'}
    auth = (settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET_ID)
    response = requests.post(token_url, data=data, auth=auth)

    if response.status_code == 200:
        print("Access Token: ", response.json()['access_token'])
        return response.json()['access_token']
    else:
        raise Exception(f"Failed to get access token from PayPal. Status code: {response.status_code}")


def paypal_payment_verify(request, billing_id):
    billing = base_models.Billing.objects.get(billing_id=billing_id)

    transaction_id = request.GET.get("transaction_id")
    print("transaction_id ====", transaction_id)
    paypal_api_url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{transaction_id}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_paypal_access_token()}'
    }

    response = requests.get(paypal_api_url, headers=headers)
    print("Response: ", response)
    print("Response Status Code: ", response.status_code)

    if response.status_code == 200:
        paypal_order_data = response.json()
        paypal_payment_status = paypal_order_data['status']

        if paypal_payment_status == "COMPLETED":
            if billing.status == "Unpaid":
                billing.status = "Paid"
                billing.save()
                billing.appointment.status = "Completed"
                billing.appointment.save()

                doctor_models.Notification.objects.create(
                    doctor=billing.appointment.doctor,
                    appointment=billing.appointment,
                    type="New Appointment"
                )

                patient_models.Notification.objects.create(
                    patient=billing.appointment.patient,
                    appointment=billing.appointment,
                    type="Appointment Scheduled"
                )

                merge_data = {
                    "billing": billing
                }

                # Send appointment email to doctor
                subject = "New Appointment"
                text_body = render_to_string("email/new_appointment.txt", merge_data)
                html_body = render_to_string("email/new_appointment.html", merge_data)

                # Add the try-catch to gracefully handle the case where email cannot be sent
                try:
                    msg = EmailMultiAlternatives(
                        subject=subject,
                        from_email=settings.FROM_EMAIL,
                        to=[billing.appointment.doctor.user.email],
                        body=text_body
                    )
                    msg.attach_alternative(html_body, "text/html")
                    msg.send()

                    # Send appointment booked email to patient
                    subject = "Appointment Booked Successfully"
                    text_body = render_to_string("email/appointment_booked.txt", merge_data)
                    html_body = render_to_string("email/appointment_booked.html", merge_data)

                    msg = EmailMultiAlternatives(
                        subject=subject,
                        from_email=settings.FROM_EMAIL,
                        to=[billing.appointment.patient.email],
                        body=text_body
                    )
                    msg.attach_alternative(html_body, "text/html")
                    msg.send()
                except:
                    print("Email cannot be sent now!")

                return redirect(f"/payment_status/{billing.billing_id}/?payment_status=paid")
        
        return redirect(f"/payment_status/{billing.billing_id}/?payment_status=failed")
        
    
    return redirect(f"/payment_status/{billing.billing_id}/?payment_status=failed")
    

@login_required
def payment_status(request, billing_id):
    billing = base_models.Billing.objects.get(billing_id=billing_id)
    payment_status = request.GET.get("payment_status")

    context = {
        "billing": billing,
        "payment_status": payment_status,
    }
    return render(request, "base/payment_status.html", context)

def course_detail_redirect(request, service_id):
    """Redirect legacy course-detail URLs to the service detail page"""
    return redirect('service_detail', service_id=service_id)
