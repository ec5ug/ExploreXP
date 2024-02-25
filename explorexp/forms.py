from django import forms
from .models import Place, Challenge

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['long', 'lat', 'name', 'type']

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'category', 'description', 'place', 'points']
