from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    owner = models.EmailField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    isComplete = models.CharField(max_length=200)
    collaborators = models.IntegerField(default=0)
    def __str__(self):
            return self.title


class Users(models.Model):
    email = models.EmailField(max_length=50)
    fl_name = models.CharField(max_length=50)
    hashed_password = models.CharField(max_length=50)

    def __str__(self):
            return self.email

class Users2(models.Model):
    user = models.OneToOneField(User)

    fl_name = models.CharField(
        verbose_name='First and Last Name',
        max_length=50,
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'fl_name']

    def __unicode__(self):
        return self.user.username
