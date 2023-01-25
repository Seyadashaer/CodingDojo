from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        "all_dojos": models.get_all_dojos(),
        "ninjas": models.get_all_ninjas()
    }

    return render(request, 'index.html', context)

def new_dojo(request):
    models.add_dojo(request)
    return redirect('/')

def new_ninja(request):
    models.add_ninja(request)
    return redirect('/')

