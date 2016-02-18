from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    owner = models.EmailField(max_length=50)
    title = models.CharField(max_length=2000, help_text="Please enter task title")
    description = models.CharField(max_length=2000, help_text="Please enter task description")
    isComplete = models.BooleanField(default=False)
    collaborator1 = models.EmailField(max_length=50, blank=True)
    collaborator2 = models.EmailField(max_length=50, blank=True)
    collaborator3 = models.EmailField(max_length=50, blank=True) #do I need to change this to link with Users model?
    def __str__(self):
            return self.title


# class Users(models.Model):
#     email = models.EmailField(max_length=50)
#     fl_name = models.CharField(max_length=50)
#     hashed_password = models.CharField(max_length=50)
#
#     def __str__(self):
#             return self.email
