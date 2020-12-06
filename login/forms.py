
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile

title= [
    ('student', 'Student'),
    ('faculty', 'Faculty'),
    ('others', 'Others'),
    ]
INTEGER_CHOICES= [tuple([x,x]) for x in range(1,150)]

class CreateUserForm(UserCreationForm):
    occupation= forms.CharField(label='select your professional title', widget=forms.Select(choices=title))
    age = forms.IntegerField(label="select age", widget=forms.Select(choices=INTEGER_CHOICES))
    college = forms.CharField()
    field_of_study = forms.CharField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'age', 'occupation', 'college', 'field_of_study', 'username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']