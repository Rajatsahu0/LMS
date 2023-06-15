from socket import fromshare
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=10)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
class CareerContact(forms.Form):
    
    name = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=10)
    email = forms.EmailField()
    select= forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)