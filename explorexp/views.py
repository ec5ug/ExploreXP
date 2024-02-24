# homepage/views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import generic, View
from .models import Category, UserProfile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import PlaceForm
from django.views import generic, View
from .models import Category, Place
from django.http import JsonResponse
from django.template.defaultfilters import slugify


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
            return redirect('')  # Redirect to a success page
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


def view_profile(request, username):
    user_found = User.objects.get(username=username)
    #user_profile, created = UserProfile.objects.get_or_create(user=username)
    context = {
        "USER_PROFILE": user_found,
        #"CHALLENGES": profile.challenges_completed.all()
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

