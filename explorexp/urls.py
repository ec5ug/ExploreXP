"""explorexp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import get_locations, PlacePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('map/', views.map, name="map"),
    path('add_place/', views.add_place, name="add_place"),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('get_locations/', get_locations, name='get_locations'),
    path('placePage/<str:name_slug>/', PlacePageView.as_view(), name='placePage'),
]