from django import forms
from django.forms import ModelForm
from django.db import models
#from .models import Venue

  
class VenueForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Venue
        #venue = models.ForeignKey('venue')
        fields = '__all__'