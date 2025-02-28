import os
import django
import sys
from datetime import datetime

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

from userauths.models import User
from doctor.models import Doctor
from django.utils.dateparse import parse_datetime

def list_users():
    """List all users in the system"""
    users = User.objects.all()
    print("\nAll users in the system:")
    print("-" * 70)
    print(f"{'ID':<5} {'Username':<20} {'Email':<30} {'Is Staff':<10}")
    print("-" * 70)
    
    for user in users:
        print(f"{user.id:<5} {user.username:<20} {user.email or 'No email':<30} {'Yes' if user.is_staff else 'No':<10}")
    
    print("\n")

def create_doctor_for_user(user_id):
    """Create a doctor profile for an existing user"""
    try:
        # Find the user by ID
        user = User.objects.get(id=user_id)
        print(f"Found user: {user.username} (ID: {user.id})")
        
        # Check if doctor profile already exists
        if Doctor.objects.filter(user=user).exists():
            print(f"Doctor profile already exists for {user.username}")
            return
        
        # Create doctor profile
        doctor = Doctor.objects.create(
            user=user,
            created_at=datetime.now()
        )
        print(f"Doctor profile created for {user.username} (ID: {doctor.id})")
    except User.DoesNotExist:
        print(f"User with ID {user_id} does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list_users":
        list_users()
    elif command == "create_doctor_for_user":
        if len(sys.argv) < 3:
            print("Usage: python script.py create_doctor_for_user <user_id>")
            sys.exit(1)
        user_id = int(sys.argv[2])
        create_doctor_for_user(user_id)
    else:
        print(f"Unknown command: {command}")
        print("Available commands: list_users, create_doctor_for_user")
        sys.exit(1)
