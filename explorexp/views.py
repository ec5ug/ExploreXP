# homepage/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

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


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
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


class PlacePageView(View):
    template_name = 'placePage.html'

    def get(self, request, name_slug):
        place = get_object_or_404(Place, name_slug=name_slug)
        return render(request, self.template_name, {'place': place})
