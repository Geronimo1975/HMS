from apps.user.models import User


users = [
    {"username": "chris92", "is_active": False},
    {"username": "chris", "is_active": True},
    {"username": "alice67", "is_active": True},
    {"username": "bob", "is_active": True},
    {"username": "mike", "is_active": False},
    {"username": "jane93", "is_active": True},
    {"username": "john", "is_active": True},
    {"username": "mary", "is_active": True},
]


for data in users:
    User.objects.create(**data)

print("Inserted with success")




