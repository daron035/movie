from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import *

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    
    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'editContent', 'placeholder': "Enter your email..."}),
        }
        labels = {
            'email': ''
        }