from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(

    )


class NewUserForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class usersForm(forms.ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your username here...',
    }))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your email here...',
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your first name here...',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your last name here...',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


# user profile form
class UserProfileForm(forms.ModelForm):
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your location here...',
    }))
    mobile = forms.CharField(label='Phone Number', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your Phoe number here...',
    }))
    region = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your Region here...',
    }))
    district = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your district here...',
    }))
    ward = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Write your ward here...',
    }))

    class Meta:
        model = UserProfile
        fields = ('image', 'location', 'mobile',
                  'region', 'district', 'ward')
