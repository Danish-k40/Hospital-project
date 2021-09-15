from django.db import models

# Create your models here.
from django.db import models
from app.models import *
import datetime


# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateField(default=datetime.date.today)
    health = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    msg = models.TextField()

    def __str__(self):
        return self.name
