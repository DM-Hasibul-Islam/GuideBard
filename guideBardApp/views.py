from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import settings, logout


def homePage(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signUp(request):
    return render(request, 'sign-up.html')


def login(request):
    return render(request, 'login.html')


def tourGuide(request):
    return render(request, 'tour-guides.html')


def reviews(request):
    return render(request, 'review.html')


def profile(request):
    return render(request, 'profile.html')


def contacts(request):
    return render(request, 'contacts.html')


def payment(request):
    return render(request, 'home.html')


def tourist_spots(request):
    return render(request, 'tourist-spots.html')


def register(request):
    return render(request, 'sign-up.html')