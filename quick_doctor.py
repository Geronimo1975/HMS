import os
import django
from datetime import datetime

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

from userauths.models import User
from doctor.models import Doctor

def create_doctor_for_current_user():
    """Create doctor profile for the current logged-in user"""
    
    # Get the currently logged in user - we'll use the most recent one
    latest_user = User.objects.filter(last_login__isnull=False).order_by('-last_login').first()
    
    if not latest_user:
        print("No users with login history found. Using first available user.")
        latest_user = User.objects.first()
    
    if not latest_user:
        print("No users found in the database!")
        return
    
    print(f"Creating doctor profile for user: {latest_user.username} (ID: {latest_user.id})")
    
    # Check if doctor already exists
    if Doctor.objects.filter(user=latest_user).exists():
        print(f"Doctor profile already exists for {latest_user.username}")
        return
    
    # Create doctor profile with default image
    doctor = Doctor.objects.create(
        user=latest_user,
        full_name=f"Dr. {latest_user.first_name} {latest_user.last_name}" if latest_user.first_name and latest_user.last_name else f"Dr. {latest_user.username}",
        image="images/default_doctor.jpg",
        mobile="+49234567890",
        country="Germany",
        bio="Experienced medical professional",
        specialization="General Medicine",
        qualifications="MD",
        years_of_experience="5",
        next_available_appointment_date=datetime.now()
    )
    
    print(f"SUCCESS: Created doctor profile for {latest_user.username} (ID: {latest_user.id})")
