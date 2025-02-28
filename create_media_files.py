import os
import shutil
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

def setup_media_directories():
    """Set up media directories and add default images"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    media_dir = os.path.join(base_dir, 'media')
    images_dir = os.path.join(media_dir, 'images')
    
    # Create directories if they don't exist
    print("Setting up media directories...")
    os.makedirs(images_dir, exist_ok=True)
    
    # Create a simple default image if it doesn't exist
    default_doctor_path = os.path.join(images_dir, 'default_doctor.jpg')
    default_patient_path = os.path.join(images_dir, 'default_patient.jpg')
    default_service_path = os.path.join(images_dir, 'default_service.jpg')
    
    # Check for static directory with sample images
    static_img_dir = os.path.join(base_dir, 'static', 'img')
    
    # First try to copy from static if available
    if os.path.exists(static_img_dir):
        print("Copying images from static directory...")
        # Copy doctor images
        for i in range(1, 11):
            src_file = os.path.join(static_img_dir, f'doctor{i}.jpg')
            dst_file = os.path.join(images_dir, f'doctor{i}.jpg')
            if os.path.exists(src_file) and not os.path.exists(dst_file):
                shutil.copy(src_file, dst_file)
                print(f"Copied {dst_file}")
        
        # Copy patient images
        for i in range(1, 11):
            src_file = os.path.join(static_img_dir, f'patient{i}.jpg')
            dst_file = os.path.join(images_dir, f'patient{i}.jpg')
            if os.path.exists(src_file) and not os.path.exists(dst_file):
                shutil.copy(src_file, dst_file)
                print(f"Copied {dst_file}")
                
        # Copy service images
        for i in range(1, 11):
            src_file = os.path.join(static_img_dir, f'service{i}.jpg')
            dst_file = os.path.join(images_dir, f'service{i}.jpg')
            if os.path.exists(src_file) and not os.path.exists(dst_file):
                shutil.copy(src_file, dst_file)
                print(f"Copied {dst_file}")
    
    # Create blank default images if needed
    if not os.path.exists(default_doctor_path):
        with open(default_doctor_path, 'wb') as f:
            # Create a simple 1x1 pixel JPEG
            f.write(bytes([
                0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01,
                0x01, 0x01, 0x00, 0x48, 0x00, 0x48, 0x00, 0x00, 0xFF, 0xDB, 0x00, 0x43,
                0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 0x07, 0x07, 0x09,
                0x09, 0x08, 0x0A, 0x0C, 0x14, 0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12,
                0x13, 0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A, 0x1C, 0x1C, 0x20,
                0x24, 0x2E, 0x27, 0x20, 0x22, 0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29,
                0x2C, 0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27, 0x39, 0x3D, 0x38, 0x32,
                0x3C, 0x2E, 0x33, 0x34, 0x32, 0xFF, 0xC0, 0x00, 0x0B, 0x08, 0x00, 0x01,
                0x00, 0x01, 0x01, 0x01, 0x11, 0x00, 0xFF, 0xC4, 0x00, 0x14, 0x00, 0x01,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x08, 0xFF, 0xC4, 0x00, 0x14, 0x10, 0x01, 0x00, 0x00,
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x00, 0x00, 0xFF, 0xDA, 0x00, 0x08, 0x01, 0x01, 0x00, 0x00, 0x3F, 0x00,
                0xD2, 0xCF, 0x20, 0xFF, 0xD9
            ]))
        print(f"Created default doctor image at {default_doctor_path}")
    
    # Create the same default image for patients and services if needed
    if not os.path.exists(default_patient_path):
        shutil.copy(default_doctor_path, default_patient_path)
        print(f"Created default patient image at {default_patient_path}")
        
    if not os.path.exists(default_service_path):
        shutil.copy(default_doctor_path, default_service_path)
        print(f"Created default service image at {default_service_path}")

if __name__ == "__main__":
    setup_media_directories()
