import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

# Import models after Django setup
from doctor.models import Doctor
from userauths.models import User
from query.doctor import sync_doctors_to_db

def test_doctor_sync():
    print("Running doctor sync...")
    # Clear existing doctors for a clean test
    # Doctor.objects.all().delete()
    # User.objects.filter(user_type="Doctor").delete()
    
    # Run the sync function
    sync_doctors_to_db()
    
    # Check if doctors were created
    doctors = Doctor.objects.all()
    print(f"Found {doctors.count()} doctors in database")
    
    # Print details of each doctor
    for doctor in doctors:
        print(f"ID: {doctor.id}, Name: {doctor.full_name}, Specialization: {doctor.specialization}")
        print(f"  Mobile: {doctor.mobile}, Country: {doctor.country}")
        print(f"  User ID: {doctor.user_id}, Username: {doctor.user.username}")
        print("-------------------")

if __name__ == "__main__":
    test_doctor_sync()
