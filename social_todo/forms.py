from django import forms
from social_todo.models import Task, User#, Users2 ,UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class NewTaskForm(forms.ModelForm):
    # An inline class to provide additional information on the form.

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Task
        fields = ('title', 'description', 'collaborator1', 'collaborator2', 'collaborator3')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class MyRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password')
