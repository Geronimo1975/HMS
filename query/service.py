from base.models import Service
from doctor.models import Doctor
from django.utils import timezone

def sync_services_to_db():
    """Sync Django Service model data to PostgreSQL using Django ORM"""
    
    # Create services
    service_data = [
        {
            'id': 1,
            'image': 'images/service1.jpg',
            'name': 'Cardiology Consultation',
            'description': 'Comprehensive heart health assessment and consultation',
            'cost': 150.00
        },
        {
            'id': 2,
            'image': 'images/service2.jpg',
            'name': 'Pediatric Check-up',
            'description': 'Complete health examination for children',
            'cost': 100.00
        },
        {
            'id': 3,
            'image': 'images/service3.jpg',
            'name': 'Orthopedic Evaluation',
            'description': 'Assessment of bone and joint conditions',
            'cost': 130.00
        },
        {
            'id': 4,
            'image': 'images/service4.jpg',
            'name': 'Dermatology Screening',
            'description': 'Comprehensive skin examination and consultation',
            'cost': 120.00
        },
        {
            'id': 5,
            'image': 'images/service5.jpg',
            'name': 'Neurological Assessment',
            'description': 'Evaluation of neurological functions and disorders',
            'cost': 160.00
        },
        {
            'id': 6,
            'image': 'images/service6.jpg',
            'name': 'Prenatal Care',
            'description': 'Pregnancy monitoring and maternal health services',
            'cost': 140.00
        },
        {
            'id': 7,
            'image': 'images/service7.jpg',
            'name': 'Psychiatric Consultation',
            'description': 'Mental health assessment and counseling',
            'cost': 170.00
        },
        {
            'id': 8,
            'image': 'images/service8.jpg',
            'name': 'General Physical Examination',
            'description': 'Complete health check-up and preventive care',
            'cost': 110.00
        },
        {
            'id': 9,
            'image': 'images/service9.jpg',
            'name': 'Vision Testing',
            'description': 'Comprehensive eye examination',
            'cost': 90.00
        },
        {
            'id': 10,
            'image': 'images/service10.jpg',
            'name': 'Endocrinology Consultation',
            'description': 'Assessment of hormone-related conditions',
            'cost': 145.00
        }
    ]
    
    print("Creating services...")
    
    # Create service-doctor relationships
    service_doctor_mapping = [
        (1, 1), # Cardiology - Dr. James Wilson
        (2, 2), # Pediatrics - Dr. Sarah Johnson
        (3, 3), # Orthopedics - Dr. Michael Brown
        (4, 4), # Dermatology - Dr. Emily Davis
        (5, 5), # Neurology - Dr. David Miller
        (6, 6), # Obstetrics - Dr. Linda Wilson
        (7, 7), # Psychiatry - Dr. Robert Taylor
        (8, 8), # Family Medicine - Dr. Jennifer Anderson
        (9, 9), # Ophthalmology - Dr. William Thomas
        (10, 10), # Endocrinology - Dr. Elizabeth Jackson
        (8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
        (8, 6), (8, 7), (8, 9), (8, 10)
    ]
    
    for data in service_data:
        # Create or update service
        service, created = Service.objects.update_or_create(
            id=data['id'],
            defaults={
                'image': data['image'],
                'name': data['name'],
                'description': data['description'],
                'cost': data['cost']
            }
        )
        
        action = "Created" if created else "Updated"
        print(f"{action} service: {service.name}")
    
    # Associate doctors with services
    print("Mapping doctors to services...")
    for service_id, doctor_id in service_doctor_mapping:
        try:
            service = Service.objects.get(id=service_id)
            doctor = Doctor.objects.get(id=doctor_id)
            service.available_doctors.add(doctor)
            print(f"Added {doctor.full_name} to {service.name}")
        except (Service.DoesNotExist, Doctor.DoesNotExist) as e:
            print(f"Error: {e}")

def get_doctor_services():
    """Get services offered by each doctor using Django ORM"""
    doctors = Doctor.objects.all()
    
    return [
        {
            'doctor_id': doctor.id,
            'doctor_name': doctor.full_name,
            'specialization': doctor.specialization,
            'services': [service.name for service in doctor.service_set.all()]
        }
        for doctor in doctors
    ]
