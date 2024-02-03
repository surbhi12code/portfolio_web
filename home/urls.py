from django.contrib import admin
from django.urls import path,include
from home import views
from .views import contactModel
urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects'),
    
    
]
