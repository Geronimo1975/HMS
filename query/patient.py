from patient.models import Patient
from userauths.models import User
from django.utils.dateparse import parse_date

def sync_patients_to_db():
    """Sync Django Patient model data to PostgreSQL using Django ORM"""
    
    # Create patient users and their profiles
    patient_data = [
        {
            'user_id': 12,
            'email': 'patient1@example.com',
            'username': 'patient1',
            'first_name': 'John',
            'last_name': 'Doe',
            'full_name': 'John Doe',
            'image': 'images/patient1.jpg',
            'mobile': '+49876543210',
            'address': '123 Main St, Anytown',
            'gender': 'Male',
            'dob': '1980-05-15',
            'blood_group': 'A+'
        },
        {
            'user_id': 13,
            'email': 'patient2@example.com',
            'username': 'patient2',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'full_name': 'Jane Smith',
            'image': 'images/patient2.jpg',
            'mobile': '+49876543211',
            'address': '456 Oak Ave, Somewhere',
            'gender': 'Female',
            'dob': '1975-08-22',
            'blood_group': 'O-'
        },
        # Add all remaining patients here
        {
            'user_id': 14,
            'email': 'patient3@example.com',
            'username': 'patient3',
            'first_name': 'Robert',
            'last_name': 'Johnson',
            'full_name': 'Robert Johnson',
            'image': 'images/patient3.jpg',
            'mobile': '+49876543212',
            'address': '789 Pine Rd, Nowhere',
            'gender': 'Male',
            'dob': '1990-03-10',
            'blood_group': 'B+'
        },
        {
            'user_id': 15,
            'email': 'patient4@example.com',
            'username': 'patient4',
            'first_name': 'Maria',
            'last_name': 'Garcia',
            'full_name': 'Maria Garcia',
            'image': 'images/patient4.jpg',
            'mobile': '+49876543213',
            'address': '321 Elm St, Anywhere',
            'gender': 'Female',
            'dob': '1988-11-05',
            'blood_group': 'AB-'
        },
        {
            'user_id': 16,
            'email': 'patient5@example.com',
            'username': 'patient5',
            'first_name': 'James',
            'last_name': 'Brown',
            'full_name': 'James Brown',
            'image': 'images/patient5.jpg',
            'mobile': '+49876543214',
            'address': '654 Maple Dr, Somewhere',
            'gender': 'Male',
            'dob': '1965-07-30',
            'blood_group': 'A-'
        },
        {
            'user_id': 17,
            'email': 'patient6@example.com',
            'username': 'patient6',
            'first_name': 'Patricia',
            'last_name': 'Miller',
            'full_name': 'Patricia Miller',
            'image': 'images/patient6.jpg',
            'mobile': '+49876543215',
            'address': '987 Cedar Ln, Anytown',
            'gender': 'Female',
            'dob': '1992-01-18',
            'blood_group': 'O+'
        },
        {
            'user_id': 18,
            'email': 'patient7@example.com',
            'username': 'patient7',
            'first_name': 'Michael',
            'last_name': 'Davis',
            'full_name': 'Michael Davis',
            'image': 'images/patient7.jpg',
            'mobile': '+49876543216',
            'address': '159 Birch Ave, Nowhere',
            'gender': 'Male',
            'dob': '1978-09-25',
            'blood_group': 'B-'
        },
        {
            'user_id': 19,
            'email': 'patient8@example.com',
            'username': 'patient8',
            'first_name': 'Linda',
            'last_name': 'Wilson',
            'full_name': 'Linda Wilson',
            'image': 'images/patient8.jpg',
            'mobile': '+49876543217',
            'address': '753 Walnut St, Anywhere',
            'gender': 'Female',
            'dob': '1983-04-12',
            'blood_group': 'AB+'
        },
        {
            'user_id': 20,
            'email': 'patient9@example.com',
            'username': 'patient9',
            'first_name': 'David',
            'last_name': 'Martinez',
            'full_name': 'David Martinez',
            'image': 'images/patient9.jpg',
            'mobile': '+49876543218',
            'address': '246 Pine Ave, Somewhere',
            'gender': 'Male',
            'dob': '1970-12-08',
            'blood_group': 'A+'
        },
        {
            'user_id': 21,
            'email': 'patient10@example.com',
            'username': 'patient10',
            'first_name': 'Elizabeth',
            'last_name': 'Anderson',
            'full_name': 'Elizabeth Anderson',
            'image': 'images/patient10.jpg',
            'mobile': '+49876543219',
            'address': '135 Oak St, Anytown',
            'gender': 'Female',
            'dob': '1986-06-20',
            'blood_group': 'O-'
        }
    ]
    
    print("Creating patients...")
    
    for data in patient_data:
        # Get or create the user first
        user, created = User.objects.get_or_create(
            id=data['user_id'],
            defaults={
                'email': data['email'],
                'username': data['username'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                'user_type': 'Patient',
                'password': 'password'
            }
        )
        
        # Then create or update the patient profile
        patient, created = Patient.objects.update_or_create(
            user=user,
            defaults={
                'full_name': data['full_name'],
                'image': data['image'],
                'mobile': data['mobile'],
                'address': data['address'],
                'gender': data['gender'],
                'dob': parse_date(data['dob']),
                'blood_group': data['blood_group'],
                'email': data['email']
            }
        )
        
        action = "Created" if created else "Updated"
        print(f"{action} patient: {patient.full_name}")

def fetch_patients_with_doctors():
    """Fetch patients with their assigned doctors using Django ORM"""
    from base.models import Appointment
    from doctor.models import Doctor
    
    patients_with_doctors = []
    
    for patient in Patient.objects.all():
        # Get the latest appointment for this patient
        appointment = Appointment.objects.filter(patient=patient).order_by('-appointment_date').first()
        
        if appointment:
            patients_with_doctors.append({
                'patient_id': patient.id,
                'patient_name': patient.full_name,
                'patient_email': patient.email,
                'doctor_name': appointment.doctor.full_name,
                'specialization': appointment.doctor.specialization
            })
    
    return patients_with_doctors
