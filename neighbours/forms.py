from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighborhood,Occupants,Business
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']
        help_texts = {
            'username': '',
            'email': '',
            'password1':'',
            'password2':''
        }
        help_texts={'username':'','email':'','password1':'','password2':''}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Occupants
        exclude=['name']


class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude = ['owner','neighborhood']

