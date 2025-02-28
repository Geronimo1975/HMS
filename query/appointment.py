from base.models import Appointment, MedicalRecord, LabTest, Prescription, Billing
from doctor.models import Doctor
from patient.models import Patient
from base.models import Service
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import uuid

def sync_appointments_to_db():
    """Sync Django Appointment model data to PostgreSQL using Django ORM"""
    
    # First, let's print the available fields to debug
    print("Available fields in Appointment model:", [f.name for f in Appointment._meta.fields])
    
    appointment_data = [
        {
            'id': 1,
            'appointment_date': '2024-03-01 09:30:00',
            'description': 'Chest pain and shortness of breath', # Changed from 'reason'
            'notes': 'Pain when exercising, occasional dizziness', # Changed from 'symptoms'
            'appointment_id': '123456',
            'status': 'Scheduled',
            'patient_id': 1,
            'doctor_id': 1,
            'service_id': 1
        },
        {
            'id': 2,
            'appointment_date': '2024-03-01 10:45:00',
            'description': 'Routine pediatric check-up', # Changed from 'reason'
            'notes': 'No symptoms, regular annual visit', # Changed from 'symptoms'
            'appointment_id': '234567',
            'status': 'Scheduled',
            'patient_id': 2,
            'doctor_id': 2,
            'service_id': 2
        },
        {
            'id': 3,
            'appointment_date': '2024-03-02 14:00:00',
            'description': 'Right knee pain after sports injury', # Changed from 'reason'
            'notes': 'Swelling, limited range of motion', # Changed from 'symptoms'
            'appointment_id': '345678',
            'status': 'Scheduled',
            'patient_id': 3,
            'doctor_id': 3,
            'service_id': 3
        },
        {
            'id': 4,
            'appointment_date': '2024-03-02 15:30:00',
            'description': 'Skin rash and itching', # Changed from 'reason'
            'notes': 'Red patches on arms and legs, severe itching at night', # Changed from 'symptoms'
            'appointment_id': '456789',
            'status': 'Scheduled',
            'patient_id': 4,
            'doctor_id': 4,
            'service_id': 4
        },
        {
            'id': 5,
            'appointment_date': '2024-03-03 11:15:00',
            'description': 'Recurring headaches', # Changed from 'reason'
            'notes': 'Intense pain behind eyes, sensitivity to light', # Changed from 'symptoms'
            'appointment_id': '567890',
            'status': 'Scheduled',
            'patient_id': 5,
            'doctor_id': 5,
            'service_id': 5
        },
        {
            'id': 6,
            'appointment_date': '2024-03-04 09:00:00',
            'description': 'Pregnancy follow-up', # Changed from 'reason'
            'notes': 'No complications, routine 20-week check-up', # Changed from 'symptoms'
            'appointment_id': '678901',
            'status': 'Scheduled',
            'patient_id': 6,
            'doctor_id': 6,
            'service_id': 6
        },
        {
            'id': 7,
            'appointment_date': '2024-03-04 13:45:00',
            'description': 'Depression and anxiety symptoms', # Changed from 'reason'
            'notes': 'Trouble sleeping, persistent sad mood, fatigue', # Changed from 'symptoms'
            'appointment_id': '789012',
            'status': 'Scheduled',
            'patient_id': 7,
            'doctor_id': 7,
            'service_id': 7
        },
        {
            'id': 8,
            'appointment_date': '2024-03-05 16:00:00',
            'description': 'Annual physical examination', # Changed from 'reason'
            'notes': 'No specific issues, routine health monitoring', # Changed from 'symptoms'
            'appointment_id': '890123',
            'status': 'Scheduled',
            'patient_id': 8,
            'doctor_id': 8,
            'service_id': 8
        },
        {
            'id': 9,
            'appointment_date': '2024-03-06 11:00:00',
            'description': 'Vision problems, blurry sight', # Changed from 'reason'
            'notes': 'Difficulty reading and driving at night', # Changed from 'symptoms'
            'appointment_id': '901234',
            'status': 'Scheduled',
            'patient_id': 9,
            'doctor_id': 9,
            'service_id': 9
        },
        {
            'id': 10,
            'appointment_date': '2024-03-06 14:30:00',
            'description': 'Weight gain and fatigue', # Changed from 'reason'
            'notes': 'Unexplained weight gain and constant tiredness', # Changed from 'symptoms'
            'appointment_id': '012345',
            'status': 'Scheduled',
            'patient_id': 10,
            'doctor_id': 10,
            'service_id': 10
        }
    ]
    
    print("Creating appointments...")
    
    for data in appointment_data:
        try:
            patient = Patient.objects.get(id=data['patient_id'])
            doctor = Doctor.objects.get(id=data['doctor_id'])
            service = Service.objects.get(id=data['service_id'])
            
            appointment_date = timezone.make_aware(parse_datetime(data['appointment_date']))
            
            # Create a dictionary with only the fields that exist in the model
            appointment_fields = {
                'appointment_date': appointment_date,
                'appointment_id': data['appointment_id'],
                'status': data['status'],
                'patient': patient,
                'doctor': doctor,
                'service': service
            }
            
            # Try to add these fields if they exist in your model
            if hasattr(Appointment, 'description'):
                appointment_fields['description'] = data['description']
            elif hasattr(Appointment, 'reason'):
                appointment_fields['reason'] = data['description']
                
            if hasattr(Appointment, 'notes'):
                appointment_fields['notes'] = data['notes']
            elif hasattr(Appointment, 'symptoms'):
                appointment_fields['symptoms'] = data['notes']
            
            # Create or update appointment with only valid fields
            appointment, created = Appointment.objects.update_or_create(
                id=data['id'],
                defaults=appointment_fields
            )
            
            action = "Created" if created else "Updated"
            print(f"{action} appointment: {appointment.appointment_id} for {patient.full_name} with Dr. {doctor.full_name}")
            
        except (Patient.DoesNotExist, Doctor.DoesNotExist, Service.DoesNotExist) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error creating appointment: {str(e)}")

def get_patient_appointment_history():
    """Get appointment history for all patients with medical records using Django ORM"""
    appointments = Appointment.objects.select_related(
        'patient', 'doctor', 'service'
    ).prefetch_related('medicalrecord_set')
    
    history = []
    
    for appointment in appointments:
        medical_record = appointment.medicalrecord_set.first()
        
        history.append({
            'patient': appointment.patient.full_name,
            'appointment_date': appointment.appointment_date,
            'doctor': appointment.doctor.full_name,
            'service': appointment.service.name,
            'diagnosis': medical_record.diagnosis if medical_record else None,
            'treatment': medical_record.treatment if medical_record else None,
            'status': appointment.status
        })
    
    return history

def get_doctor_schedule():
    """Get schedule for all doctors using Django ORM"""
    appointments = Appointment.objects.select_related('doctor', 'patient').all()
    
    schedule = []
    
    for appointment in appointments:
        schedule.append({
            'doctor': appointment.doctor.full_name,
            'appointment_date': appointment.appointment_date,
            'patient': appointment.patient.full_name,
            'reason': appointment.reason,
            'status': appointment.status
        })
    
    return schedule
