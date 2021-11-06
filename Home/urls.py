from django.contrib import admin
from django.urls import path, include
from Home import views

urlpatterns = [
    path("", views.index, name= 'Home'),
    path("Services", views.services, name= 'Services'),
    path("about", views.about, name= 'about'),
    path("contact", views.contact, name= 'contact'),
    path("chocolates", views.chocolates, name= 'chocolates'),
    path("icecreams", views.icecreams, name= 'icecreams'),
    path("coffee", views.coffee, name= 'coffee'),
    path("pastriesandwaffles", views.pastriesandwaffles, name= 'pastriesandwaffles'),
]
