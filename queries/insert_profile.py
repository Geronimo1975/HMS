from apps.user.models import User, Profile
from apps.resources.models import Resources

#backward relation you have also for one-to-one

#find the user by username and create the profile
#user = models.OneToOneField(
       # "user.User", on_delete=models.CASCADE, unique=True)

#user = (the field)
#on the right side you have reference to the table user and the primary key id of the user 

users = User.objects.filter(username__in=["chris92", "chris","alice67"])
#I filter the users with this query you create the object users 

for user in users: #I catch every user in users and I pass it in user = user 
    #create a profile for each user 
    Profile.objects.create(
        user = user, #if you change the name of the fild you must change here (before the = comes from the model)
        bio=f"Bio for {user.username}",
        age=25
    )

print("Profile created successfully!")

#user = user
#to pass the entire object because Django automatically crate the connection with the primary key of user
#user_id = user.id 

#practice with the querying line in checking_resources 


