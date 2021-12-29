from django.db import models
from django.db.models.fields import *
from django.db import models

# Create your models here.

class user_data(models.Model):
    name = CharField(max_length=50)
    email = EmailField(max_length=50)
    password = CharField(max_length=80)


    def __str__(self):
        return self.name
