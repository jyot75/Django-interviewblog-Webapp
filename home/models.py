from django.db import models
from accounts.models import NewUser
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, null=True, blank=False)
    year = models.IntegerField(null=True, blank=False)
    job_offer = models.CharField(max_length=25, choices=[("Summer Internship",'Summer Internship'),("Winter Internship & Job",'Winter Internship & Job'), ("Job",'Job'), ("Winter Internship Only",'Winter Internship Only')], null=True, blank=False)
    profile = models.CharField(max_length=255, null=True, blank=False)
    title = models.CharField(max_length=255, null=True, blank=False, unique=True)
    body = RichTextField(null=True, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    bookmark = models.ManyToManyField(NewUser, related_name='bookmark', default=None, blank=True)
    
    def get_absolute_url(self):
        return reverse('explore')
    