from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

#def index(request):
#    return HttpResponse("Hello World")

def index(request):
    return render(request, "index.html")

def forum(request):
    return render(request, "forum.html")

