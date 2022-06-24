from pathlib import Path
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    Path('', views.index, name='index'),
]
