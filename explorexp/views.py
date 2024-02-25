# homepage/views.py
from datetime import datetime
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import generic, View
from datetime import datetime

from auth_app import models
from .models import Category, UserProfile, Post, Challenge
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import PlaceForm, ChallengeForm, PostForm
from django.views import generic, View
from .models import Category, Place
from django.http import JsonResponse
from django.template.defaultfilters import slugify
import re

def home(request):
    return render(request, 'home.html')


def map(request):
    key = request.session.get("API_KEY")
    context = {
        'key': key,
    }
    return render(request, 'map.html', context)


def index(request):
    return render(request, 'index.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page
    else:
        form = PlaceForm()
    return render(request, 'add_place.html', {'form': form})


class CategoriesView(generic.ListView):
    template_name = "categories.html"
    context_object_name = "categories"

    def get_queryset(self):
        """
        Return the list of categories.
        """
        return Category.objects.all()


def get_locations(request):
    selected_category = request.GET.get('category', '')

    # Fetch data from the Place model based on the selected category
    places = Place.objects.filter(type=selected_category).values('name', 'lat', 'long')

    # Convert the queryset to a list and prepare the response
    locations = list(places)
    response_data = {'locations': locations}

    return JsonResponse(response_data)


def view_profile(request, username):
    user_found = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user_found)
    challenges_completed = Challenge.objects.filter(post__in=posts)
    total_points_completed = challenges_completed.aggregate(total_points=Sum('points'))['total_points'] or 0
    badges = dict()
    for challenge in challenges_completed:
        if challenge.category.name == 'Libraries':
            badges['Libraries'] = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzRyNTNxNGE2dTQ0bnBwdTQ4ejc1bm56cjFwaWZwN2twZTBwd29lMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4KGVH1hRpRke7ZnaUv/giphy.gif'
        if challenge.category.name == 'Café':
            badges['Café'] = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGZ0cTFkbWJ6MnBsMnU2aDI2MzlxOG41bHg3YXE3OHEybDI1aG4zdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/oZTBoGcs5dcXhaiYxz/giphy.gif"

    context = {
        "USER_PROFILE": user_found,
        "CHALLENGES_COMPLETED": challenges_completed,
        "total_points_completed": total_points_completed,
        "USER_POSTS": posts,
        "BADGES": badges
    }
    return render(request, 'profile.html', context=context)


def get_locations(request):
    selected_category = request.GET.get('category', '')

    # Fetch data from the Place model based on the selected category
    places = Place.objects.filter(type=selected_category).values('name', 'lat', 'long')

    # Convert the queryset to a list and prepare the response
    locations = list(places)
    response_data = {'locations': locations}

    return JsonResponse(response_data)


class PlacePageView(View):
    template_name = 'placePage.html'

    def get(self, request, name_slug):
        name = re.sub('[^0-9a-zA-Z]+', '-', name_slug)
        place = get_object_or_404(Place, name_slug=name)
        print(place)
        context = {
            "PLACE": place,
            "NAME_SLUG": name_slug
        }
        return render(request, self.template_name, {'place': place})


def view_place(request):
    if request.method == 'POST':
        if 'user' in request.POST.keys():
            uo = User.objects.filter(username=request.POST['user'])[0]
            po = Place.objects.filter(name=request.POST['place'])[0]
            co = Challenge.objects.filter(name=request.POST['challenge'])[0]
            do = datetime.now()
            other_response = request.POST.copy()
            other_response['user'] = uo
            other_response['place'] = po
            other_response['challenge'] = co
            other_response['date'] = do
            form = PostForm(other_response)
            if form.is_valid():
                form.save()
        else:
            p_obj = Place.objects.filter(name=request.POST['place'])[0]
            c_obj = Category.objects.filter(name=request.POST['category'])[0]
            alt_response = request.POST.copy()
            alt_response['place'] = p_obj
            alt_response['category'] = c_obj
            form = ChallengeForm(alt_response)
            if form.is_valid():
                form.save()
        location_name = request.POST['place']
    else:
        location_name = request.GET.get('name_slug', '')

    name = re.sub('[^0-9a-zA-Z]+', '-', location_name)
    place_obj = Place.objects.filter(name=location_name)[0]
    challenges = Challenge.objects.filter(place=place_obj)
    chronicles = Post.objects.filter(place=place_obj)
    context = {
        "PLACE_NAME": location_name,
        "CHALLENGES": challenges,
        "CHRONICLES": chronicles,
        "PLACE_OBJECT": place_obj
    }
    return render(request, 'placePage.html', context)
