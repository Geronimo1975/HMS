from django.shortcuts import render, redirect
from django.contrib import messages

def about_us(request):
    return render(request, "pages/about-us.html")

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you could add code to send an email or save to database
        
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact_us')
        
    return render(request, "pages/contact-us.html")

# Create your views here.
