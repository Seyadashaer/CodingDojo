from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(request):
    context = {
        "All_users" : models.get_all_users()
    }
    return render(request, 'index.html', context)


def create_user(request):
        first_name_from_form = request.POST['first_name']
        last_name_from_form = request.POST['last_name']
        email_from_form = request.POST['email_address']
        age_from_form = request.POST['age']

        models.create_user(first_name_from_form, last_name_from_form, email_from_form, age_from_form)

        return redirect("/")
