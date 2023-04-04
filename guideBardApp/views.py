from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import forms, authenticate, AuthenticationForm
from django.forms.formsets import formset_factory
from django.contrib.auth import settings, logout
from django.contrib.auth.models import User


def homePage(request):
    return render(request, 'home.html')


def signUp(request):
    return render(request, 'sign-up.html')


def login(request):
    return render(request, 'login.html')


def tourGuide(request):
    return render(request, 'tour-guide.html')


def reviews(request):
    return render(request, 'review.html')


def profile(request):
    return render(request, 'profile.html')


def contacts(request):
    return render(request, 'contacts.html')


def payment(request):
    return render(request, 'home.html')


def login_request(request):
    global username, password
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")