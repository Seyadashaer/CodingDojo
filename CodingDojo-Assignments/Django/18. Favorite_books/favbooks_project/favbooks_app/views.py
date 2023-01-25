from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User , Book
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
        return redirect('/books')

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
        return redirect('/books')

def books(request):
    context = {
        'user': models.get_user(request, id=id),
        "books": models.get_all_books()

    }
    return render(request, 'books.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')


def home(request):
    return redirect('/books')

def add_book(request): 
    errors = Book.objects.validate_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        models.add_book(request)
        return redirect("/books")

def view_book(request, id):
    book = models.get_book(id=id)
    user_id = book.uploaded_by.id

    if user_id == request.session['id']:
        context = {
        "book": book,
        "user": models.get_user(request, id=id),
        "all_book": models.get_all_books(),
        }
        return render(request, 'edit_book.html', context)

    else:
        context = {
        "book": book,
        "user": models.get_user(request, id=id),
        "all_book": models.get_all_books(),
        }
        return render(request, 'view_book.html', context)

def edit_book(request, id):
    errors = Book.objects.validate_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{id}')
    else:
        models.edit_book(request, id=id)
        return redirect('/books')


def delete_book(request, id):
    models.delete_book(request, id=id)
    return redirect("/books")


def add_to_favorites(request, id):
    models.add_to_favorites(request, id=id)
    return redirect(f'/books/{id}')

def remove_from_favorites(request, id):
    models.remove_from_favorites(request, id=id)
    return redirect(f'/books/{id}')

