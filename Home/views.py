from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('This is homepage')


def services(request):
    return render(request, 'services.html')
    #return HttpResponse('This is services page')


def about(request):
    return render(request, 'about.html')
   #return HttpResponse('This is about page')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Message sent!')
    
    return render(request, 'contact.html')


def chocolates(request):
    return render(request, 'chocolates.html')

def icecreams(request):
    return render(request, 'icecreams.html')

def coffee(request):
    return render(request, 'coffee.html')

def pastriesandwaffles(request):
    return render(request, 'pastriesandwaffles.html')

