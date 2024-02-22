from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render



def Home(request):
    return render(request, "Index.html")


def About(request):
    return render(request, "About.html")


def Login(request):
    return render(request, "Login.html")


def Contact(request):
    return render(request, "Contact.html")


