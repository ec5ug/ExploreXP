from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.contrib.auth.models import User

class Place(models.Model):
    long = models.DecimalField(max_digits=20, decimal_places=16)
    lat = models.DecimalField(max_digits=20, decimal_places=16)
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    name_slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Place, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    place = models.ForeignKey(Place, related_name='challenges', on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name} @ {self.place}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    date = models.DateField()
    def __str__(self):
        return f"{self.user} | {self.challenge}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    challenges_completed = models.ManyToManyField(Challenge, related_name='challenges_completed', blank=True)

    def __str__(self):
        return self.user.username
