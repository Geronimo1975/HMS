import psycopg2

def sync_complete_structure():
    """Create complete database structure matching Django models"""
    try:
        conn = psycopg2.connect(
            dbname="hms_db",
            user="postgres",
            password="Secet1975", 
            host="localhost"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Create many-to-many junction table for services and doctors
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS base_service_available_doctors (
            id SERIAL PRIMARY KEY,
            service_id INTEGER REFERENCES base_service(id),
            doctor_id INTEGER REFERENCES doctor_doctor(id)
        );
        """)
        
        # Create medical record table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS base_medicalrecord (
            id SERIAL PRIMARY KEY,
            diagnosis TEXT,
            treatment TEXT,
            appointment_id INTEGER REFERENCES base_appointment(id)
        );
        """)
        
        # Create lab test table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS base_labtest (
            id SERIAL PRIMARY KEY,
            test_name VARCHAR(255),
            description TEXT,
            result TEXT,
            appointment_id INTEGER REFERENCES base_appointment(id)
        );
        """)
        
        # Create prescription table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS base_prescription (
            id SERIAL PRIMARY KEY,
            medications TEXT,
            appointment_id INTEGER REFERENCES base_appointment(id)
        );
        """)
        
        # Create billing table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS base_billing (
            id SERIAL PRIMARY KEY,
            sub_total DECIMAL(10,2),
            tax DECIMAL(10,2),
            total DECIMAL(10,2),
            status VARCHAR(20),
            billing_id VARCHAR(10),
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            patient_id INTEGER REFERENCES patient_patient(id),
            appointment_id INTEGER REFERENCES base_appointment(id)
        );
        """)
        
        # Create doctor notification table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctor_notification (
            id SERIAL PRIMARY KEY,
            type VARCHAR(100),
            seen BOOLEAN DEFAULT FALSE,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            doctor_id INTEGER REFERENCES doctor_doctor(id),
            appointment_id INTEGER REFERENCES base_appointment(id)
        );
        """)
        
        # Create patient notification table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient_notification (
            id SERIAL PRIMARY KEY,
            type VARCHAR(100),
            seen BOOLEAN DEFAULT FALSE,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            patient_id INTEGER REFERENCES patient_patient(id),
            appointment_id INTEGER REFERENCES base_appointment(id)
        );
        """)
        
        print("Successfully created all tables matching Django models!")
        
        # List all tables
        cursor.execute("""
        SELECT table_name FROM information_schema.tables 
        WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()
        print("\nAvailable tables in database:")
        for table in tables:
            print(f"- {table[0]}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    sync_complete_structure()
