from django import forms
from social_todo.models import Tasks, UserProfile
from django.contrib.auth.models import User
from django import forms

class NewTaskForm(forms.ModelForm):
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tasks
        fields = ('title', 'description', 'collaborators')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('website')
