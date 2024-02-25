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
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views
from .views import get_locations

urlpatterns = [
    path('map/', views.map, name="map"),
    path('admin/', admin.site.urls),
    path('app/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name="index"),
    path('accounts/', include('allauth.urls')),

    path('logout/', views.logout_view, name='logout'),
    path('home', views.home, name="home"),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
    path('add_place/', views.add_place, name="add_place"),
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('get_locations/', get_locations, name='get_locations'),

]