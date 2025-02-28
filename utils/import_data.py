from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from userauths.models import User
from doctor.models import Doctor
from patient.models import Patient
from base.models import Service, Appointment, MedicalRecord, LabTest, Prescription

def run():
    # Create users first (they are referenced by other models)
    print("Creating users...")
    
    # Create admin user if not exists
    if not User.objects.filter(email='admin@hms.com').exists():
        User.objects.create_superuser(email='admin@hms.com', username='admin', password='SecurePassword123')
    
    # Create doctor users
    doctor_users = [
        {'id': 2, 'email': 'doctor1@hms.com', 'username': 'doctor1', 'first_name': 'James', 'last_name': 'Wilson', 'user_type': 'Doctor'},
        {'id': 3, 'email': 'doctor2@hms.com', 'username': 'doctor2', 'first_name': 'Sarah', 'last_name': 'Johnson', 'user_type': 'Doctor'},
        {'id': 4, 'email': 'doctor3@hms.com', 'username': 'doctor3', 'first_name': 'Michael', 'last_name': 'Brown', 'user_type': 'Doctor'},
        {'id': 5, 'email': 'doctor4@hms.com', 'username': 'doctor4', 'first_name': 'Emily', 'last_name': 'Davis', 'user_type': 'Doctor'},
        {'id': 6, 'email': 'doctor5@hms.com', 'username': 'doctor5', 'first_name': 'David', 'last_name': 'Miller', 'user_type': 'Doctor'},
    ]
    
    for data in doctor_users:
        User.objects.get_or_create(
            id=data['id'], 
            defaults={
                'email': data['email'],
                'username': data['username'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'user_type': data['user_type'],
                'password': 'pbkdf2_sha256$600000$ABCDEFG1234567890'  # Placeholder password hash
            }
        )
    
    # Create doctors
    print("Creating doctors...")
    doctor_data = [
        {'user_id': 2, 'full_name': 'Dr. James Wilson', 'image': 'images/doctor1.jpg', 'mobile': '+49234567890', 'country': 'Germany', 'bio': 'Experienced cardiologist', 'specialization': 'Cardiology', 'qualifications': 'MD, FACC', 'years_of_experience': '15'},
        {'user_id': 3, 'full_name': 'Dr. Sarah Johnson', 'image': 'images/doctor2.jpg', 'mobile': '+49234567891', 'country': 'France', 'bio': 'Pediatric specialist', 'specialization': 'Pediatrics', 'qualifications': 'MD, FAAP', 'years_of_experience': '12'},
        {'user_id': 4, 'full_name': 'Dr. Michael Brown', 'image': 'images/doctor3.jpg', 'mobile': '+49234567892', 'country': 'Italy', 'bio': 'Sports medicine expert', 'specialization': 'Orthopedics', 'qualifications': 'MD, FAAOS', 'years_of_experience': '10'},
        {'user_id': 5, 'full_name': 'Dr. Emily Davis', 'image': 'images/doctor4.jpg', 'mobile': '+49234567893', 'country': 'Spain', 'bio': 'Skin specialist', 'specialization': 'Dermatology', 'qualifications': 'MD, FAAD', 'years_of_experience': '8'},
        {'user_id': 6, 'full_name': 'Dr. David Miller', 'image': 'images/doctor5.jpg', 'mobile': '+49234567894', 'country': 'United Kingdom', 'bio': 'Headache specialist', 'specialization': 'Neurology', 'qualifications': 'MD, PhD', 'years_of_experience': '14'},
    ]
    
    for data in doctor_data:
        user = User.objects.get(id=data['user_id'])
        Doctor.objects.get_or_create(
            user=user,
            defaults={
                'full_name': data['full_name'],
                'image': data['image'], 
                'mobile': data['mobile'], 
                'country': data['country'],
                'bio': data['bio'],
                'specialization': data['specialization'],
                'qualifications': data['qualifications'],
                'years_of_experience': data['years_of_experience']
            }
        )
    
    # Create patient users and patients
    # Add other models (Service, Appointment, etc.)
    # Similar pattern for patients, appointments, etc.
    
    print("Data import completed successfully!")

if __name__ == "__main__":
    run()
