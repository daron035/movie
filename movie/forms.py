from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import *

class AddReviewForm(forms.ModelForm):
    """ Форма добавления отзывов """
    captcha = ReCaptchaField()
    
    class Meta:
        model = Reviews
        fields = ('text', 'name', 'email', 'captcha')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border'}),
            'text': forms.Textarea(attrs={'class': 'form-control border'}),
        }
        
class RatingForm(forms.ModelForm):
    """ Форма добавления рейтинга """
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(),
        widget=forms.RadioSelect(),
        empty_label=None
    )
    
    class Meta:
        model = Rating
        fields = ('star',)
        
class AddMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'poster': forms.ClearableFileInput(attrs={'multiple': True})
        }