from django.db import models
from accounts.models import NewUser

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, null=True, blank=True)
    month_year = models.DateField(null=True, blank=True)
    job_offer = models.CharField(max_length=255, null=True, blank=True)
    profile = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    

