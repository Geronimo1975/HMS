from django.db import models

# Create your models here.


class Resources(models.Model):
    # foreign key, is a relationship between the resources table and the user table in the app user
    user = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    # user app name---> User is the class name

    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=500, unique=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"

# we are linking two different models.
#one-to-many User(one)-Resources(many)

