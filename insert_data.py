import psycopg2
import sys
from datetime import datetime

def insert_sample_data():
    """Insert sample data into the HMS database tables"""
    
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname="hms_db",
            user="postgres",
            password="Secet1975", 
            host="localhost"
        )
        
        # Create a cursor and start transaction
        cursor = conn.cursor()
        print("Connected to database. Starting data insertion...")
        
        # Insert doctors with explicit columns
        print("Inserting doctors...")
        doctor_data = [
            (1, 'Dr. James Wilson', 'images/doctor1.jpg', '+49234567890', 'Germany', 'Experienced cardiologist', 'Cardiology', 'MD, FACC', '15', '2024-03-01 09:00:00', 2),
            (2, 'Dr. Sarah Johnson', 'images/doctor2.jpg', '+49234567891', 'France', 'Pediatric specialist', 'Pediatrics', 'MD, FAAP', '12', '2024-03-01 10:00:00', 3)
        ]
        
        for doctor in doctor_data:
            try:
                cursor.execute("""
                INSERT INTO doctor_doctor 
                (id, full_name, image, mobile, country, bio, specialization, qualifications, years_of_experience, next_available_appointment_date, user_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """, doctor)
                print(f"Added doctor: {doctor[1]}")
            except Exception as e:
                print(f"Error adding doctor {doctor[1]}: {e}")
        
        # Insert patients
        print("\nInserting patients...")
        patient_data = [
            (1, 'John Doe', 'images/patient1.jpg', '+49876543210', '123 Main St, Anytown', 'Male', '1980-05-15', 'A+', 'patient1@example.com', 12),
            (2, 'Jane Smith', 'images/patient2.jpg', '+49876543211', '456 Oak Ave, Somewhere', 'Female', '1975-08-22', 'O-', 'patient2@example.com', 13)
        ]
        
        for patient in patient_data:
            try:
                cursor.execute("""
                INSERT INTO patient_patient 
                (id, full_name, image, mobile, address, gender, dob, blood_group, email, user_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """, patient)
                print(f"Added patient: {patient[1]}")
            except Exception as e:
                print(f"Error adding patient {patient[1]}: {e}")
        
        # Insert services
        print("\nInserting services...")
        service_data = [
            (1, 'Cardiology Consultation', 'images/service1.jpg', 'Comprehensive heart health assessment', 150.00),
            (2, 'Pediatric Check-up', 'images/service2.jpg', 'Complete health examination for children', 100.00)
        ]
        
        for service in service_data:
            try:
                cursor.execute("""
                INSERT INTO base_service 
                (id, name, image, description, cost)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """, service)
                print(f"Added service: {service[1]}")
            except Exception as e:
                print(f"Error adding service {service[1]}: {e}")
        
        # Insert appointments
        print("\nInserting appointments...")
        appointment_data = [
            (1, '2024-03-01 09:30:00', 'Chest pain', 'Shortness of breath', '123456', 'Scheduled', 1, 1, 1),
            (2, '2024-03-01 10:45:00', 'Annual check-up', 'No symptoms', '234567', 'Scheduled', 2, 2, 2)
        ]
        
        for appt in appointment_data:
            try:
                cursor.execute("""
                INSERT INTO base_appointment 
                (id, appointment_date, issues, symptoms, appointment_id, status, patient_id, doctor_id, service_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
                """, appt)
                print(f"Added appointment: {appt[4]}")
            except Exception as e:
                print(f"Error adding appointment {appt[4]}: {e}")
        
        # Commit the transaction
        conn.commit()
        print("\nAll data inserted successfully!")
        
        # Check data was inserted
        cursor.execute("SELECT COUNT(*) FROM doctor_doctor;")
        doctor_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM patient_patient;")
        patient_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM base_service;")
        service_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM base_appointment;")
        appointment_count = cursor.fetchone()[0]
        
        print(f"\nDatabase now contains: {doctor_count} doctors, {patient_count} patients, {service_count} services, {appointment_count} appointments")
        
    except Exception as e:
        print(f"Database error: {e}")
        conn.rollback()
        sys.exit(1)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    insert_sample_data()
