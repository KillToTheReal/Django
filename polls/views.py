from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style=\"display: flex; justify-content:center; margin-top: 12%; color: #222;\">Main-page </h1>")
