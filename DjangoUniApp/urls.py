from pathlib import Path
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.feed, name='feed'),
    Path('', views.index, name='index'),
]
