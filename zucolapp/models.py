from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class registration(models.Model):
    user = models.CharField(max_length=50)
    Travel_date = models.DateField()
    Phone_number = models.IntegerField()