from django import forms 
from .models import *
  
class Form(forms.ModelForm): 
  
    class Meta: 
        model = image
        fields = ['tag','img']