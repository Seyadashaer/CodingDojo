from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Pie
from . import models


def index(request):
    return render(request, 'index.html')

def login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    else:
        user = User.objects.filter(email=request.POST['email'])
        request.session['id'] = user[0].id
        return redirect('/dashboard')

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
        user = User.objects.filter(email=request.POST['email'])
        request.session['id'] = user[0].id
        return redirect('/dashboard')

def dashboard(request):
    context = {
        'user': models.get_current_user(request),
        'user_pies' : models.get_user_pies(request)
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def show_pie(request, id): 
    context = { 
        "pie" : models.get_pie(id=id),
        "user": models.get_current_user(request)
    }
    return render(request, "show.html", context)

def edit_pie_page(request, id):
    context = { 
        "pie" : models.get_pie(id=id)
    }
    return render(request, "edit.html", context)

def delete_pie(request, id):
    pie = models.get_pie(id=id)
    pie.delete()
    return redirect('/dashboard')


def show_all_pies(request):

    context = {
        "all_pies": models.get_all_pies().order_by("votes")

        
    }
    return render(request, "pies.html", context)




def add_pie(request):
    errors = Pie.objects.validate_pie(request.POST)
    if errors:  
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')


    else:
        models.add_pie(request)  
        return redirect('/dashboard')


def add_vote(request, id):
    models.add_vote(request, id=id)
    return redirect(f'/show/{id}')
    

def remove_vote(request, id):
    models.remove_vote(request, id=id)
    return redirect(f'/show/{id}')


def edit_pie(request, id):
    errors = Pie.objects.validate_pie(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{id}')
    else:
        models.edit_pie(request, id=id)
        return redirect('/dashboard')



