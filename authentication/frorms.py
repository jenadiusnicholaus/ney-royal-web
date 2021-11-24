from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(

    )


class NewUserForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()



