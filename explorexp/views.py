# homepage/views.py

from django.shortcuts import render
from django.views import generic, View
from .models import Category, Place
from django.http import JsonResponse
from django.template.defaultfilters import slugify

def home(request):
    return render(request, 'home.html')


def map(request):
    key = request.session.get("API_KEY")
    context = {
        'key':key,
    }
    return render(request, 'map.html', context)

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

    # Perform a query to retrieve locations based on the selected category
    # Replace this with your actual model and filtering logic
    places = Place.objects.filter(category=selected_category).values('name', 'lat', 'long')

    return JsonResponse({'locations': list(places)})