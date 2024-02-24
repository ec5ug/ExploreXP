# homepage/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import generic, View

from django.db.models import Sum
from .models import Category, UserProfile, Post
from django.contrib.auth.models import User


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


class CategoriesView(generic.ListView):
    template_name = "categories.html"
    context_object_name = "categories"

    def get_queryset(self):
        """
        Return the list of categories.
        """
        return Category.objects.all()


def view_profile(request, username):
    user_found = get_object_or_404(User, username=username)
    user_profile, created = UserProfile.objects.get_or_create(user=user_found)
    challenges_completed = user_profile.challenges_completed.all()
    total_points_completed = user_profile.challenges_completed.aggregate(total_points=Sum('points'))[
                                 'total_points'] or 0
    posts = Post.objects.filter(user=user_found)

    context = {
        "USER_PROFILE": user_found,
        "CHALLENGES_COMPLETED": challenges_completed,
        "total_points_completed": total_points_completed,
        "USER_POSTS": posts

    }
    return render(request, 'profile.html', context=context)
