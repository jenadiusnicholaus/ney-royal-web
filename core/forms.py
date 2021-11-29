from django import forms
from django.forms import fields
from django.contrib.auth.models import User

from core.models import Applications


class ApllicationForm(forms.ModelForm):

    class Meta:
        model = Applications
        fields = ('courses', 'file')
