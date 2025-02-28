import os
import django
import sys

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

from userauths.models import User
from doctor.models import Doctor
from django.utils import timezone

def show_all_users():
    """Display all users in the system"""
    users = User.objects.all()
    if not users:
        print("No users found in the database!")
        return None
        
    print("\nAll Users:")
    print("=" * 60)
    print(f"{'ID':<5} {'Username':<20} {'Email':<25} {'Last Login':<20}")
    print("-" * 60)
    
    for user in users:
        print(f"{user.id:<5} {user.username:<20} {user.email or 'N/A':<25} {user.last_login or 'Never'}")
    
    return users

def create_doctor_profile(username):
    """Create doctor profile for a specific username"""
    try:
        user = User.objects.get(username=username)
        print(f"\nFound user: {user.username} (ID: {user.id})")
        
        # Check if profile exists
        existing = Doctor.objects.filter(user=user).first()
        if existing:
            print(f"Doctor profile already exists: {existing.full_name}")
            return existing
            
        # Create profile
        doctor = Doctor.objects.create(
            user=user,
            full_name=f"Dr. {user.first_name} {user.last_name}" if user.first_name and user.last_name else f"Dr. {user.username}",
            image="images/default_doctor.jpg",
            mobile="+49123456789",
            country="Germany",
            bio="Experienced healthcare professional",
            specialization="General Medicine",
            qualifications="MD",
            years_of_experience="5",
            next_available_appointment_date=timezone.now()
        )
        
        print(f"\nSUCCESS: Created doctor profile")
        print(f"- Name: {doctor.full_name}")
        print(f"- Image: {doctor.image}")
        print(f"- Specialization: {doctor.specialization}")
        
        return doctor
        
    except User.DoesNotExist:
        print(f"ERROR: User '{username}' not found!")
    except Exception as e:
        print(f"ERROR: {str(e)}")
        
if __name__ == "__main__":
    # Show all users
    show_all_users()
    
    if len(sys.argv) > 1:
        # Use username from command line argument
        username = sys.argv[1]
    else:
        # Ask for username
        username = input("\nEnter username to create doctor profile for: ")
    
    create_doctor_profile(username)
