from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# from django.dispatch import receiver

# class CustomUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     degree = models.CharField(max_length=6,choices=[("1",'B.TECH'),("2",'M.TECH'),("3",'MSC')], null=True, blank=True) 
#     year = models.PositiveIntegerField(null=True, blank=True, unique=False)
#     program = models.CharField(max_length=255, null=True, blank=True, unique=False)

#     def __str__(self):
#         return self.user.username


# @receiver(models.signals.post_save, sender = User)
# def user_is_created(sender, instance, created, **kwargs):
#     if created:
#         CustomUser.objects.create(user= instance)      





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    degree = models.CharField(max_length=6,choices=[("1",'B.TECH'),("2",'M.TECH'),("3",'MSC')], null=True, blank=True) 
    year = models.PositiveIntegerField(null=True, blank=True, unique=False)
    program = models.CharField(max_length=255, null=True, blank=True, unique=False)
    
    def __str__(self):
        return f'{self.user.username} Profile'