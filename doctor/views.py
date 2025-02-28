from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from doctor import models as doctor_models
from base import models as base_models

@login_required
def dashboard(request):
    try:
        doctor = doctor_models.Doctor.objects.get(user=request.user)
        appointments = base_models.Appointment.objects.filter(doctor=doctor)
        notifications = doctor_models.Notification.objects.filter(doctor=doctor)

        context = {
            "appointments": appointments,
            "notifications": notifications,
        }

        return render(request, "doctor/dashboard.html", context)
    
    except doctor_models.Doctor.DoesNotExist:
        # Handle case when user doesn't have a doctor profile
        messages.warning(request, "You don't have a doctor profile set up yet.")
        
        # Option 1: Show doctor registration form
        return render(request, "doctor/register_doctor.html", {
            "title": "Complete Your Doctor Profile",
            "message": "Please complete your profile to continue as a doctor."
        })
        
        # Option 2: Redirect to home
        # return redirect('/')


@login_required
def appointments(request):
    try:
        doctor = doctor_models.Doctor.objects.get(user=request.user)
        appointments = base_models.Appointment.objects.filter(doctor=doctor)

        context = {
            "appointments": appointments,
        }

        return render(request, "doctor/appointments.html", context)
    except doctor_models.Doctor.DoesNotExist:
        messages.error(request, "You don't have a doctor profile yet. Please contact the administrator.")
        # Use an absolute URL instead of a named URL pattern
        return redirect('/')  # Redirect to the root URL


@login_required
def appointment_detail(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    
    medical_records = base_models.MedicalRecord.objects.filter(appointment=appointment)
    lab_tests = base_models.LabTest.objects.filter(appointment=appointment)
    prescriptions = base_models.Prescription.objects.filter(appointment=appointment)

    context = {
        "appointment": appointment,
        "medical_records": medical_records,
        "lab_tests": lab_tests,
        "prescriptions": prescriptions,
    }

    return render(request, "doctor/appointment_detail.html", context)


@login_required
def cancel_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Cancelled"
    appointment.save()

    messages.success(request, "Appointment Cancelled Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def activate_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Scheduled"
    appointment.save()

    messages.success(request, "Appointment Re-Scheduled Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def complete_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Completed"
    appointment.save()

    messages.success(request, "Appointment Completed Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def add_medical_report(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        treatment = request.POST.get("treatment")
        base_models.MedicalRecord.objects.create(appointment=appointment, diagnosis=diagnosis, treatment=treatment)

    
    messages.success(request, "Medical Report Added Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)

@login_required
def edit_medical_report(request, appointment_id, medical_report_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    medical_report = base_models.MedicalRecord.objects.get(id=medical_report_id, appointment=appointment)

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        treatment = request.POST.get("treatment")

        medical_report.diagnosis = diagnosis
        medical_report.treatment = treatment
        medical_report.save()

    messages.success(request, "Medical Report Updated Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def add_lab_test(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    if request.method == "POST":
        test_name = request.POST.get("test_name")
        description = request.POST.get("description")
        result = request.POST.get("result")

        base_models.LabTest.objects.create(appointment=appointment, test_name=test_name, description=description, result=result)

    messages.success(request, "Lab report Added Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def edit_lab_test(request, appointment_id, lab_test_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    lab_test = base_models.LabTest.objects.get(id=lab_test_id, appointment=appointment)

    if request.method == "POST":
        test_name = request.POST.get("test_name")
        description = request.POST.get("description")
        result = request.POST.get("result")

        lab_test.test_name = test_name
        lab_test.description = description
        lab_test.result = result
        lab_test.save()

    messages.success(request, "Lab Report Updated Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def add_prescription(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    if request.method == "POST":
        medications = request.POST.get("medications")
        base_models.Prescription.objects.create(medications=medications, appointment=appointment)

    messages.success(request, "Prescription Added Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def edit_prescription(request, appointment_id, prescription_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    prescription = base_models.Prescription.objects.get(id=prescription_id)

    if request.method == "POST":
        medications = request.POST.get("medications")
        prescription.medications = medications
        prescription.save()

    messages.success(request, "Prescription Updated Successfully")
    return redirect("doctor:appointment_detail", appointment.appointment_id)

@login_required
def payments(request):
    try:
        doctor = doctor_models.Doctor.objects.get(user=request.user)
        
        # Get payments related to this doctor
        appointments = base_models.Appointment.objects.filter(doctor=doctor)
        billings = base_models.Billing.objects.filter(appointment__in=appointments)
        
        context = {
            "billings": billings
        }
        
        return render(request, "doctor/payments.html", context)
        
    except doctor_models.Doctor.DoesNotExist:
        # Redirect to doctor registration page
        messages.warning(request, "Please set up your doctor profile first")
        return redirect('/doctor/')  # Redirect to dashboard


@login_required
def notifications(request):
    try:
        doctor = doctor_models.Doctor.objects.get(user=request.user)
        notifications = doctor_models.Notification.objects.filter(doctor=doctor)
        
        context = {
            "notifications": notifications
        }
        
        return render(request, "doctor/notifications.html", context)
        
    except doctor_models.Doctor.DoesNotExist:
        # Redirect to doctor registration page
        messages.warning(request, "Please set up your doctor profile first")
        return redirect('/doctor/')  # Redirect to dashboard


@login_required
def mark_noti_seen(request, id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    notification = doctor_models.Notification.objects.get(doctor=doctor, id=id)
    notification.seen = True
    notification.save()
    
    messages.success(request, "Notification marked as seen")
    return redirect("doctor:notifications")


@login_required
def profile(request):
    try:
        doctor = doctor_models.Doctor.objects.get(user=request.user)
        
        # Handle profile view logic
        if request.method == "POST":
            # Process profile update form
            doctor.full_name = request.POST.get("full_name")
            doctor.email = request.POST.get("email") 
            doctor.mobile = request.POST.get("mobile")
            doctor.specialization = request.POST.get("specialization")
            doctor.qualifications = request.POST.get("qualifications")
            doctor.years_of_experience = request.POST.get("years_of_experience")
            doctor.bio = request.POST.get("bio")
            
            # Handle image upload if provided
            if "image" in request.FILES:
                doctor.image = request.FILES["image"]
                
            doctor.save()
            messages.success(request, "Profile updated successfully")
            
        context = {
            "doctor": doctor
        }
        
        return render(request, "doctor/profile.html", context)
        
    except doctor_models.Doctor.DoesNotExist:
        # Redirect to doctor registration/setup page
        messages.warning(request, "Please set up your doctor profile first")
        return redirect('/doctor/')  # Redirect to dashboard which will show the registration form
