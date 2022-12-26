from django.shortcuts import render, redirect
from . import models
from .models import Show
from django.contrib import messages


def index(request): 
    return render(request, 'add_show.html')
    
def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        models.add_show(request)
        return redirect("/shows")


def view_all_shows(request):
    context={
        "all_shows": models.get_all_shows()
    }
    return render(request, "all_shows.html", context)

def view_show(request, id):
    context = {
        "show" : models.get_show(id)
    }
    return render(request, 'view_show.html', context)

def edit_show(request, id):
    context = {
        "all_shows": models.get_all_shows(),
        "show" : models.get_show(id),
        "release_date": str(models.get_show(id).release_date)
    }
    return render(request, 'edit_show.html', context)

def submit_edit(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        models.submit_edit(request, id)
        return redirect("/shows")

def delete_show(request, id):
    show = models.get_show(id)
    show.delete()
    return redirect("/shows")