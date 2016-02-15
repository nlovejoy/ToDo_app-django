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

# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance.
#     user = models.OneToOneField(User)
#
#     # Override the __unicode__() method to return out something meaningful!
#     def __unicode__(self):
#         return self.user.username

class Users(models.Model):
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    hashed_password = models.CharField(max_length=50)

    def __str__(self):
            return self.title

# var stringField = {
#     type: String,
#     minlength: 1,
#     maxlength: 5000
# }
#
# var TaskSchema = new Schema({
#     owner: ObjectId,
#     title: stringField,
#     description: stringField,
#     isComplete: Boolean,
#     collaborators: [String]
# });
