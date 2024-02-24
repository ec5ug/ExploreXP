from django import forms
from .models import Place

class PlaceForm(forms.Form):
    class Meta:
        model = Place
        fields = ['long', 'lat', 'name']
