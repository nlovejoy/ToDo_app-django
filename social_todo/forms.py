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
    # username = forms.EmailField(max_length=50, min_length=1)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password')

    # def clean(self):
    #     cleaned_data = super(MyRegistrationForm, self).clean()
    #     username = cleaned_data.get("username")
    #     first_name = cleaned_data.get("first_name")
    #     password = cleaned_data.get("password")
    #
    #     if len(request.POST['email']) < 1:
    #         raise ValidationError('Invalid email address, must be longer than 1')
    #     if len(request.POST['email']) < 50:
    #         raise ValidationError('Invalid email address, must be shorter than 50')
    #     return data
