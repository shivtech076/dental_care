from django.forms import ModelForm
from django import forms
from .models import UserContact

# from phonenumber_field.formfields import PhoneNumberField


class Userform(ModelForm):
    class Meta:
        model = UserContact
        fields = ['name', 'city', 'problem','phone']