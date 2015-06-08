from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Artly says hey there world!")
