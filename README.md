# Hospital Management System

A comprehensive HMS built with Django.

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd HMS
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django
pip install -r requirements.txt
```

4. Create Django project:
```bash
django-admin startproject hms_prj .

4.1 Create Django project:

```bash
python manage.py runserver 8001


```bash
python manage.py startapp base
```

5. Create necessary apps:
```bash
python manage.py startapp accounts
python manage.py startapp appointments
python manage.py startapp patients
python manage.py startapp doctors
python manage.py startapp staff
python manage.py startapp billing
python manage.py startapp pharmacy
python manage.py startapp reports
```

6. Update settings.py:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local apps
    'accounts',
    'appointments',
    'patients',
    'doctors',
    'staff',
    'billing',
    'pharmacy',
    'reports',
]
```

7. Setup database:
```bash
python manage.py makemigrations
python manage.py migrate
```

8. Create superuser:
```bash
python manage.py createsuperuser
```

9. Run development server:
```bash
python manage.py runserver
```

## Available Commands

### Make Commands
- `make help` - Show available make commands
- `make install` - Install project dependencies
- `make run` - Run development server
- `make clean` - Remove Python compiled files
- `make test` - Run tests
- `make lint` - Run code linting
- `make migrations` - Create database migrations
- `make migrate` - Apply database migrations
- `make show-migrations` - Show migrations status
- `make shell` - Open Django shell
- `make superuser` - Create superuser
- `make static` - Collect static files
- `make setup` - Complete development setup

### Django Management Commands
```bash
# Database Operations
python manage.py makemigrations    # Create migrations
python manage.py migrate           # Apply migrations
python manage.py showmigrations    # Show migrations status

# Development Server
python manage.py runserver         # Run development server
python manage.py runserver 8080    # Run on specific port

# User Management
python manage.py createsuperuser   # Create superuser
python manage.py changepassword    # Change user password

# Shell and Database
python manage.py shell             # Open Django shell
python manage.py dbshell           # Open database shell

# Static Files
python manage.py collectstatic     # Collect static files

# Testing
python manage.py test              # Run all tests
python manage.py test app_name     # Test specific app
```

## Project Structure
```
hms/
├── accounts/          # User authentication and authorization
├── appointments/      # Appointment scheduling and management
├── patients/          # Patient records and management
├── doctors/          # Doctor profiles and schedules
├── staff/            # Staff management
├── billing/          # Billing and payments
├── pharmacy/         # Medicine inventory and prescriptions
├── reports/          # Analytics and reporting
├── static/           # Static files (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/        # HTML templates
│   ├── accounts/
│   ├── appointments/
│   ├── patients/
│   └── ...
├── requirements/     # Project dependencies
│   ├── base.txt     # Base requirements
│   └── prod.txt     # Production requirements
├── manage.py        # Django management script
├── Makefile         # Project commands
└── README.md        # Project documentation
```

## Features

### Patient Management
- Patient registration and profiles
- Medical history tracking
- Appointment scheduling
- Prescription management

### Doctor Management
- Doctor profiles and specializations
- Schedule management
- Patient assignments
- Consultation records

### Appointment System
- Online appointment booking
- Schedule management
- Reminder system
- Cancellation handling

### Billing System
- Invoice generation
- Payment processing
- Insurance handling
- Financial reporting

### Pharmacy Management
- Medicine inventory
- Prescription tracking
- Stock management
- Purchase orders

### Reporting System
- Patient statistics
- Financial reports
- Inventory reports
- Appointment analytics

## Development

1. Create new app:
```bash
python manage.py startapp app_name
```

2. Make database changes:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Run tests:
```bash
make test
# or
python manage.py test
```

## Production Deployment

1. Install production requirements:
```bash
pip install -r requirements/prod.txt
```

2. Collect static files:
```bash
make static
# or
python manage.py collectstatic
```

3. Set environment variables:
```bash
export DJANGO_SETTINGS_MODULE=hms.settings.production
export DJANGO_SECRET_KEY=your-secret-key
export DJANGO_DEBUG=False
export DATABASE_URL=your-database-url
```

4. Security checklist:
- [ ] Debug mode disabled
- [ ] Secret key changed
- [ ] Database credentials secured
- [ ] HTTPS enabled
- [ ] Static files configured
- [ ] Error logging configured

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

```bash
# Run all tests
make test

# Run specific test
python manage.py test app_name.tests.test_file

# Run with coverage
coverage run manage.py test
coverage report
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

* **Your Name** - *Initial work* - [YourGithub](https://github.com/yourusername)

## Acknowledgments

* Django Documentation
* Bootstrap Templates
* Open Source Community
