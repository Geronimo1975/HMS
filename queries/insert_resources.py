from apps.user.models import User
from apps.resources.models import Resources

# create a user

# federica = User.objects.create(username='federica93', is_active=True)

# #create the resource for that user

# res1 = Resources.objects.create(user = federica, title = "Django Development",
#                                 description = "A complete guide to Django dev",
#                                 link = "http://www.djangoproject.com/")


# #user is a reference to the object and requires an object to b assigned (object property)
# #user_id is the field of our table (object user that automatically generate the id---> user_id)

# print("Success!")

# add resources for existing users

resources_data = [

    {"user": "chris", "title": "Python Tutorial",
        "description": "An introductory Python tutorial", "link": "https://www.python.org/"},
    {"user": "alice67", "title": "Machine Learning",
        "description": "Machine learning basics", "link": "https://www.ml.org/"},
    {"user": "bob", "title": "Web Development", "description": "Web development using Flask",
        "link": "https://flask.palletsprojects.com/"},
    {"user": "mike", "title": "AI Basics",
        "description": "Artificial intelligence for beginners", "link": "https://www.ai.org/"},
    {"user": "jane93", "title": "Data Science",
        "description": "Learn data science from scratch", "link": "https://www.datascience.org/"},
    {"user": "john", "title": "JavaScript Tutorial", "description": "A guide to JavaScript",
        "link": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"},
    {"user": "mary", "title": "Frontend Development",
        "description": "Frontend web development with React", "link": "https://reactjs.org/"}
]


for data in resources_data:
    # find the user based on the username
    user = User.objects.filter(username=data["user"]).first()

    if user:
        # create and insert the resources
        Resources.objects.create(
            user=user,
            title=data["title"],
            description=data["description"],
            link=data["link"]
        )

print("Success!")


#user_id = 1 (user.id) ---> not the preferred way  (field)
#ORM philosopy---> you pass the entire object user 
#user = user to link the entire user object to the resource model 
#Django automatically extracts the primary key id of the user and it stores it in the database as user_id

