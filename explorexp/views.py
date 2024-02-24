# homepage/views.py

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import logout

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
