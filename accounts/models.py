from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NewUser(AbstractUser):
    email = models.EmailField(unique=True)
    degree = models.CharField(max_length=6,choices=[("B.TECH",'B.TECH'),("M.TECH",'M.TECH'),("MSC",'MSC')], null=True, blank=False) 
    year = models.PositiveIntegerField(null=True, blank=False)
    program = models.CharField(max_length=255, null=True, blank=False)




