from django import forms
from social_todo.models import Tasks, Users #,UserProfile
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
    hashed_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Users
        fields = ('email', 'hashed_password')

class MyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email', 'fl_name', 'hashed_password')
