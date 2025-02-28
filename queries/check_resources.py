from apps.user.models import User
from apps.resources.models import Resources

# check all the resources

# resources = Resources.objects.all()
# for res in resources:
#     print(f"{res.title} - {res.description}")

# We retrieve the user instance with username federica93

# user = User.objects.get(username = "federica93")


# #we want to get the resources related to this user

# resources = Resources.objects.get(user = user) #pass the user instance

# print(resources)

# filtering resources by user

# resources = Resources.objects.filter(user__username = "federica93")
# print(resources)

# user__username uses a double __ to go from the foreign key user to the related model USER
# and filter by the username field.

# Exclude resources for a specif user

# resources = Resources.objects.exclude(user__username = "federica93")
# print(resources)


# Query looksup can span to the related tables

# resources = Resources.objects.filter(user__username__startswith = "chris")
# print(resources)

# If user is pointing to another table table 1 and table 1 is pointing to table 2
# __ you go from one table to another

# Backward relation
# A one-to-many relationship Django will automatically define a property
# named {model_name}_set as model manager .
# model manager has create (create from the main object)

# retrieve user federica93 and give one more resource her

# federica93 = User.objects.get(username="federica93")

# federica93.resources_set.create(
#     title="AWS",
#     description="AWS resource",
#     link="http://aws.amazon.com"

# )

# print("Success!")

#Forward relation: From Resources to User, you access the user of a resource via the user field. 
#child---->parent
#Bacward relation: From User to Resources, you access all the resources connected to the user using the resources_set
#parent---> child

# resource = Resources.objects.get(title = "AWS") #get a specific resource
# user = resource.user #access the user who owns this resource
# print(user.username) #print the username of the resource owner

# #forward relation: the resource model has the foreignkey(User,...) every resource belongs to the user


# user = User.objects.get(username = "federica93") #get the user
# resources = user.resources_set.all() #get all the resources linked to this user

# for resource in resources:
#     print(f"{resource.title} - {resource.description}")

# #resources_set ---> backward
# #resources_set is automatically created when we use the foregnkey
# #is useful for easy getting all the resources beloging to the user without manually filtering
# #saves you from writing a filter() query every time

# #instead of writing
# resources = Resources.objects.filter(user__username ="federica93") #---> forward

# #you can simpy do:
# resources = user.resources_set.all() #--> backward

#create() 
#resource_set.add() you already have the user and it exists in the database
#and you want to just add something to it

# user = User.objects.get(username="chris")

# res1 = Resources.objects.create(title="AWS1", description="AWS Services", link="https://aws.amazon1.com/")
# res2 = Resources.objects.create(title="Azure1", description="Azure Cloud", link="https://azure.microsoft.com/")

# user.resources_set.add(res1,res2)

# print('Success!')


#selected_related (selecting related data)

#1
resources = Resources.objects.all()
for resource in resources:
    print(resource.user.username) #this causes extra queries 

##N+ 1---> 1 query fecthes all the resources
# N additional queries fetch the user for each resource

#2

resources = Resources.objects.select_related("user").all() #uses only one query

for resource in resources:
    print(resource.user.username)

#it's like the INNER JOIN

#filter

resources = Resources.objects.select_related("user").filter(user__username = "federica93")
#user---> foreign key 

#hint for the book app
#If a model has multiple foreign key fields, you can select multiple relations:

#books = Book.objects.select_related("author", "publisher").all()


#Delete 
#it also depends on the contraint (CASCADE, NULL)
#self-study change the constraints on the foreign key and practcing the queries

resource_to_delete = Resources.objects.get(id=1)

resource_to_delete.delete()

#what happens if you delete a resource?
#what happen if you delete a user?

Resources.objects.filter(user__username = "federica93").delete()

#try the resource_set 













