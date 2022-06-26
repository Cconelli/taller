from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'clase' : 'Aprendiendo Django'}
    return HttpResponse("layout.html", context)

def feed(request):
    return render(request, 'Template/feed.html')

def profile(request):
    return render(request, 'Template/profile.html')

def register():

    return

