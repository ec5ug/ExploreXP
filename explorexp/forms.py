from django import forms
from .models import Place, Challenge, Post

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['long', 'lat', 'name', 'type']

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'category', 'description', 'place', 'points']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'place', 'challenge', 'comment', 'date']
