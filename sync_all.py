import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

# Import after Django setup
from django.db import transaction
from query.doctor import sync_doctors_to_db
from query.patient import sync_patients_to_db
from query.service import sync_services_to_db
from query.appointment import sync_appointments_to_db

def sync_all():
    # Use transaction to ensure all-or-nothing operation
    with transaction.atomic():
        print("Step 1/4: Syncing doctors (includes creating doctor users)...")
        sync_doctors_to_db()
        
        print("\nStep 2/4: Syncing patients (includes creating patient users)...")
        sync_patients_to_db()
        
        print("\nStep 3/4: Syncing services...")
        sync_services_to_db()
        
        print("\nStep 4/4: Syncing appointments...")
        sync_appointments_to_db()
        
    print("\nDatabase synchronization complete!")
    print("All data has been successfully imported to PostgreSQL.")

if __name__ == "__main__":
    sync_all()
