from django.db import models
from apps.bookstore.my_validators import maximun_no_of_awards
from apps.bookstore.enums import GenderOptions, CategoryOptions

# Create your models here.


class DateColumns(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # constraint = models.UniqueConstraint()
        # django will not creat a database table from this class


class Author(DateColumns):
    # name, email, created_at, updated_at, gender, date_of_birth, number_of_awards
    name = models.CharField(max_length=300, default="")
    email = models.EmailField(max_length=400)
    gender = models.CharField(
        max_length=20,
        choices=GenderOptions.options(),
        default=GenderOptions.default(),
    )
    date_of_birth = models.DateField(blank=True, null=True)
    #
    number_of_awards = models.PositiveSmallIntegerField(
        default=0, validators=[maximun_no_of_awards]
    )

    # send the author an email
    def save(self, *args, **kwargs):
        # hey i am gonna send and email
        super().save(*args, **kwargs)


class Book(DateColumns):
    title = models.CharField(max_length=300, default="")
    description = models.TextField(default="")
    category = models.CharField(
        max_length=50,
        choices=CategoryOptions.options(),
        default=CategoryOptions.default(),
    )
    # title, description, author( ForeignKey), created_at, updated_at, category


# - custom Object Manager
# - clean method, belongs to the model class, save()