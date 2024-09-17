from django.urls import path
from . import views









urlpatterns = [
    path('' , views.home , name='home'),
    path('about' , views.about , name='about'),
    path('partfolio' , views.partfolio , name='partfolio'),
    path('contact' , views.contact , name='contact')
]