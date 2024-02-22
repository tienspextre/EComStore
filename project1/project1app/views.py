from django.shortcuts import render
from django.http import HttpResponse

def project1app(request):
    return HttpResponse("Hello world!")
