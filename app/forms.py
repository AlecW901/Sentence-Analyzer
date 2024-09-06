from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Sentence


class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField(max_length=101)
    last_name=forms.CharField(max_length=101)
    email= forms.EmailField()

    class Meta:
        model=User
        fields= ['username','first_name','last_name','email','password1','password2']


class SentenceForm(forms.ModelForm):
    text=forms.CharField()
    class Meta:
        model=Sentence
        fields=['text']