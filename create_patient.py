import os
import django
import sys

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

from userauths.models import User
from patient.models import Patient
from django.utils.dateparse import parse_date

def list_users():
    """List all users in the system"""
    users = User.objects.all()
    print("\nAll users in the system:")
    print("-" * 70)
    print(f"{'ID':<5} {'Username':<20} {'Email':<30} {'Is Staff':<10}")
    print("-" * 70)
    
    for user in users:
        # Use is_staff instead of user_type which might be None
        print(f"{user.id:<5} {user.username:<20} {user.email or 'No email':<30} {'Yes' if user.is_staff else 'No':<10}")
    
    print("\n")

def create_patient_for_user(username):
    """Create a patient profile for an existing user"""
    try:
        # Find the user
        user = User.objects.get(username=username)
        print(f"Found user: {user.username} (ID: {user.id})")
        
        # Check if patient profile already exists
        if Patient.objects.filter(user=user).exists():
            print(f"Patient profile already exists for {username}")
            return
        
        # Create patient profile
        patient = Patient.objects.create(
            user=user,
            full_name=f"{user.first_name} {user.last_name}" if user.first_name else username,
            email=user.email,
            mobile="+49123456789",  # Default phone
            address="123 Main St, Berlin",  # Default address
            gender="Male",  # Default gender
            dob=parse_date("1990-01-01"),  # Default birth date
            blood_group="O+"  # Default blood group
        )
        print(f"Created patient profile for {username}: {patient.full_name}")
        
        return patient
    except User.DoesNotExist:
        print(f"User {username} not found!")
    except Exception as e:
        print(f"Error: {str(e)}")

def create_patient_for_user_by_id(user_id):
    """Create a patient profile for an existing user using ID"""
    try:
        # Find the user by ID (which should be unique)
        user = User.objects.get(id=user_id)
        print(f"Found user: {user.username} (ID: {user.id})")
        
        # Check if patient profile already exists
        if Patient.objects.filter(user=user).exists():
            print(f"Patient profile already exists for {user.username}")
            return
        
        # Create patient profile
        patient = Patient.objects.create(
            user=user,
            full_name=f"{user.first_name} {user.last_name}" if user.first_name and user.last_name else user.username,
            email=user.email or f"{user.username}@example.com",
            mobile="+49123456789",  # Default phone
            address="123 Main St, Berlin",  # Default address
            gender="Male",  # Default gender
            dob=parse_date("1990-01-01"),  # Default birth date
            blood_group="O+"  # Default blood group
        )
        print(f"Created patient profile for {user.username}: {patient.full_name}")
        
        return patient
    except User.DoesNotExist:
        print(f"User with ID {user_id} not found!")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # List all users
    list_users()
    
    # Get user ID from input
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
    else:
        user_id = int(input("Enter the ID of the user to create a patient profile for: "))
    
    # Create patient profile for user with given ID
    create_patient_for_user_by_id(user_id)
