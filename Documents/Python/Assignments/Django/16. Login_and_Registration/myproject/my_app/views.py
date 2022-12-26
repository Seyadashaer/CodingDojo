from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User


def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validate_register(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            )
        messages.success(request, "New User Registered")
        return redirect('/success')

def login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        messages.success(request, "User Logged In")
        return redirect('/success')

def success(request):
    return render(request, 'success.html')