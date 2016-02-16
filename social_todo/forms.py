from django import forms
from social_todo.models import Tasks, Users, Users2 #,UserProfile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class NewTaskForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tasks
        fields = ('title', 'description', 'collaborators')

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users2
        fields = ('email', 'password')

class MyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Users2
        fields = ('email', 'fl_name', 'password')
