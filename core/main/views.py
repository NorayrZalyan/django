from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    home_list = Home.objects.all()
    context = {
        'home_list':home_list
    }
    return render(request , 'home.html' , context)


def about(request):
    about_list = About.objects.all()
    context = {
        'about_list':about_list
    }
    return render(request , 'about.html' , context)


def partfolio(request):
    return render(request , 'partfolio.html')


def contact(request):
    return render(request , 'contact.html')