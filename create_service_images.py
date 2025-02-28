import os
import shutil
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hms_prj.settings")
django.setup()

def create_service_images():
    """Create numbered service images from the default service image"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    media_dir = os.path.join(base_dir, 'media')
    images_dir = os.path.join(media_dir, 'images')
    
    # Ensure the directory exists
    os.makedirs(images_dir, exist_ok=True)
    
    # Path to default service image
    default_service_path = os.path.join(images_dir, 'default_service.jpg')
    
    if not os.path.exists(default_service_path):
        print(f"Default service image not found at {default_service_path}")
        return
    
    # Create numbered service images
    for i in range(1, 11):
        service_path = os.path.join(images_dir, f'service{i}.jpg')
        if not os.path.exists(service_path):
            shutil.copy(default_service_path, service_path)
            print(f"Created service{i}.jpg")
    
    print("All service images created successfully!")

if __name__ == "__main__":
    create_service_images()
