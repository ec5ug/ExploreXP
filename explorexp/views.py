# homepage/views.py

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views import generic, View
from .models import Category

def home(request):
    return render(request, 'home.html')


def map(request):
    key = request.session.get("API_KEY")
    context = {
        'key':key,
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
