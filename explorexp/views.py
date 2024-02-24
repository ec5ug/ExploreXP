# homepage/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def map(request):
    key = env.API_KEY
    context = {
        'key':key,
    }
    return render(request, 'map.html', context)

