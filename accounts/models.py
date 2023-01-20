from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    degree = models.CharField(max_length=6,choices=[("1",'B.TECH'),("2",'M.TECH'),("3",'MSC')], null=True, blank=True) 
    year = models.PositiveIntegerField(null=True, blank=True, unique=False)
    program = models.CharField(max_length=255, null=True, blank=True, unique=False)
