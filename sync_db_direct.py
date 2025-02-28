import os
import sys
import psycopg2
from psycopg2 import sql

def sync_database_directly():
    """Directly sync database tables without Django ORM"""
    
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            dbname="hms_db",
            user="postgres",
            password="Secet1975",  # Using the password from your .env file
            host="localhost"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Create tables directly
        print("Creating tables...")
        
        # Create doctor table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctor_doctor (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            image VARCHAR(255),
            mobile VARCHAR(20),
            country VARCHAR(100),
            bio TEXT,
            specialization VARCHAR(100),
            qualifications VARCHAR(255),
            years_of_experience VARCHAR(5),
            next_available_appointment_date TIMESTAMP,
            user_id INTEGER
        );
        """)
        print("Created doctor table")
        
        # Create patient table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS patient_patient (
            id SERIAL PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            image VARCHAR(255),
            mobile VARCHAR(20),
            address TEXT,
            gender VARCHAR(10),
            dob DATE,
            blood_group VARCHAR(5),
            email VARCHAR(100),
            user_id INTEGER
        );
        """)
        print("Created patient table")
        
        # Create service table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS base_service (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            image VARCHAR(255),
            description TEXT,
            cost DECIMAL(10, 2)
        );
        """)
        print("Created service table")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sync_database_directly()
