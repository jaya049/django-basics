from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Venue
from .models import Registration

  
class VenueForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Venue
        # venue = models.ForeignKey('venue')
        fields = '__all__'

class RegistrationForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Registration
        fields = '__all__'