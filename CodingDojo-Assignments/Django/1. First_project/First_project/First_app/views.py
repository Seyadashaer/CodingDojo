from django.shortcuts import HttpResponse, redirect 
from django.http import JsonResponse

def root_method(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new_method(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create_method(request):
    return redirect("/")

def show_method(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit_method(request, number): 
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy_method(request, number): 
    return redirect("/blogs")