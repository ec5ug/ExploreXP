# homepage/views.py
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import generic, View
from .models import Category, Challenge, UserProfile, Post
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

    context = {
        "USER_PROFILE": user_found,
        "CHALLENGES_COMPLETED": challenges_completed,
        "total_points_completed": total_points_completed,
        "USER_POSTS": posts,
        "BADGES": badges
    }
    return render(request, 'profile.html', context=context)

