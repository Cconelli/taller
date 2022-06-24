from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'clase' : 'Aprendiendo Django'}
    return HttpResponse("Login.html", context)



