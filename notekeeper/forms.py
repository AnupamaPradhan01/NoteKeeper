from django import forms 
from .models import Notekeeper
class NotekeeperForm(forms.ModelForm):
    class Meta:
        model=Notekeeper
        fields=['title','description']
        