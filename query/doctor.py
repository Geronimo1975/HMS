from doctor.models import Doctor
from userauths.models import User
from django.utils.dateparse import parse_datetime

def sync_doctors_to_db():
    """Sync Django Doctor model data to PostgreSQL using Django ORM"""
    
    # Create doctor users and their profiles
    doctor_data = [
        {
            'user_id': 2,
            'email': 'doctor1@hms.com',
            'username': 'doctor1',
            'first_name': 'James',
            'last_name': 'Wilson',
            'full_name': 'Dr. James Wilson',
            'image': 'images/doctor1.jpg',
            'mobile': '+49234567890',
            'country': 'Germany',
            'bio': 'Experienced cardiologist',
            'specialization': 'Cardiology',
            'qualifications': 'MD, FACC',
            'years_of_experience': '15',
            'next_available_appointment_date': '2024-03-01 09:00:00'
        },
        {
            'user_id': 3,
            'email': 'doctor2@hms.com',
            'username': 'doctor2',
            'first_name': 'Sarah',
            'last_name': 'Johnson',
            'full_name': 'Dr. Sarah Johnson',
            'image': 'images/doctor2.jpg',
            'mobile': '+49234567891',
            'country': 'France',
            'bio': 'Pediatric specialist',
            'specialization': 'Pediatrics',
            'qualifications': 'MD, FAAP',
            'years_of_experience': '12',
            'next_available_appointment_date': '2024-03-01 10:00:00'
        },
        {
            'user_id': 4,
            'email': 'doctor3@hms.com',
            'username': 'doctor3',
            'first_name': 'Michael',
            'last_name': 'Brown',
            'full_name': 'Dr. Michael Brown',
            'image': 'images/doctor3.jpg',
            'mobile': '+49234567892',
            'country': 'Italy',
            'bio': 'Sports medicine expert',
            'specialization': 'Orthopedics',
            'qualifications': 'MD, FAAOS',
            'years_of_experience': '10',
            'next_available_appointment_date': '2024-03-01 11:00:00'
        },
        {
            'user_id': 5,
            'email': 'doctor4@hms.com',
            'username': 'doctor4',
            'first_name': 'Emily',
            'last_name': 'Davis',
            'full_name': 'Dr. Emily Davis',
            'image': 'images/doctor4.jpg',
            'mobile': '+49234567893',
            'country': 'Spain',
            'bio': 'Skin specialist',
            'specialization': 'Dermatology',
            'qualifications': 'MD, FAAD',
            'years_of_experience': '8',
            'next_available_appointment_date': '2024-03-01 13:00:00'
        },
        {
            'user_id': 6,
            'email': 'doctor5@hms.com',
            'username': 'doctor5',
            'first_name': 'David',
            'last_name': 'Miller',
            'full_name': 'Dr. David Miller',
            'image': 'images/doctor5.jpg',
            'mobile': '+49234567894',
            'country': 'United Kingdom',
            'bio': 'Headache specialist',
            'specialization': 'Neurology',
            'qualifications': 'MD, PhD',
            'years_of_experience': '14',
            'next_available_appointment_date': '2024-03-01 14:00:00'
        },
        {
            'user_id': 7,
            'email': 'doctor6@hms.com',
            'username': 'doctor6',
            'first_name': 'Linda',
            'last_name': 'Wilson',
            'full_name': 'Dr. Linda Wilson',
            'image': 'images/doctor6.jpg',
            'mobile': '+49234567895',
            'country': 'Netherlands',
            'bio': 'Prenatal care specialist',
            'specialization': 'Obstetrics',
            'qualifications': 'MD, FACOG',
            'years_of_experience': '16',
            'next_available_appointment_date': '2024-03-01 15:00:00'
        },
        {
            'user_id': 8,
            'email': 'doctor7@hms.com',
            'username': 'doctor7',
            'first_name': 'Robert',
            'last_name': 'Taylor',
            'full_name': 'Dr. Robert Taylor',
            'image': 'images/doctor7.jpg',
            'mobile': '+49234567896',
            'country': 'Switzerland',
            'bio': 'Mental health expert',
            'specialization': 'Psychiatry',
            'qualifications': 'MD, FAPA',
            'years_of_experience': '11',
            'next_available_appointment_date': '2024-03-01 16:00:00'
        },
        {
            'user_id': 9,
            'email': 'doctor8@hms.com',
            'username': 'doctor8',
            'first_name': 'Jennifer',
            'last_name': 'Anderson',
            'full_name': 'Dr. Jennifer Anderson',
            'image': 'images/doctor8.jpg',
            'mobile': '+49234567897',
            'country': 'Sweden',
            'bio': 'General health practitioner',
            'specialization': 'Family Medicine',
            'qualifications': 'MD, FAAFP',
            'years_of_experience': '9',
            'next_available_appointment_date': '2024-03-01 17:00:00'
        },
        {
            'user_id': 10,
            'email': 'doctor9@hms.com',
            'username': 'doctor9',
            'first_name': 'William',
            'last_name': 'Thomas',
            'full_name': 'Dr. William Thomas',
            'image': 'images/doctor9.jpg',
            'mobile': '+49234567898',
            'country': 'Austria',
            'bio': 'Eye specialist',
            'specialization': 'Ophthalmology',
            'qualifications': 'MD, FAAO',
            'years_of_experience': '13',
            'next_available_appointment_date': '2024-03-01 18:00:00'
        },
        {
            'user_id': 11,
            'email': 'doctor10@hms.com',
            'username': 'doctor10',
            'first_name': 'Elizabeth',
            'last_name': 'Jackson',
            'full_name': 'Dr. Elizabeth Jackson',
            'image': 'images/doctor10.jpg',
            'mobile': '+49234567899',
            'country': 'Belgium',
            'bio': 'Thyroid specialist',
            'specialization': 'Endocrinology',
            'qualifications': 'MD, FACE',
            'years_of_experience': '10',
            'next_available_appointment_date': '2024-03-01 19:00:00'
        }
    ]
    
    print("Creating doctors...")
    
    for data in doctor_data:
        # Get or create the user first
        user, created = User.objects.get_or_create(
            id=data['user_id'],
            defaults={
                'email': data['email'],
                'username': data['username'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'user_type': 'Doctor',
                'password': 'password'  # Changed from hash to simple password
            }
        )
        
        # Then create or update the doctor profile
        doctor, created = Doctor.objects.update_or_create(
            user=user,
            defaults={
                'full_name': data['full_name'],
                'image': data['image'],
                'mobile': data['mobile'],
                'country': data['country'],
                'bio': data['bio'],
                'specialization': data['specialization'],
                'qualifications': data['qualifications'],
                'years_of_experience': data['years_of_experience'],
                'next_available_appointment_date': parse_datetime(data['next_available_appointment_date'])
            }
        )
        
        action = "Created" if created else "Updated"
        print(f"{action} doctor: {doctor.full_name}")

def get_doctor_patient_count():
    """Get number of patients assigned to each doctor using Django ORM"""
    from base.models import Appointment
    from django.db.models import Count
    
    doctor_counts = Doctor.objects.annotate(
        patient_count=Count('appointment')
    ).order_by('-patient_count')
    
    return [
        {
            'doctor_id': doctor.id, 
            'doctor_name': doctor.full_name, 
            'patient_count': doctor.patient_count
        } 
        for doctor in doctor_counts
    ]
