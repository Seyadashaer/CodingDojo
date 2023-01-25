from django.shortcuts import render, redirect
from . import models
from .models import Course
from django.contrib import messages

def index(request): 
    context = {
        "All_courses": models.get_all_courses()
    }
    return render(request, 'index.html', context)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        models.add_course(request)
        return redirect('/')

def display_delete_page(request, id):
    context = {
        "course" : models.get_course(id=id)
    }
    return render(request, 'delete.html', context)


def delete_course(request, id): 
    models.delete_course(id=id)
    return redirect('/')