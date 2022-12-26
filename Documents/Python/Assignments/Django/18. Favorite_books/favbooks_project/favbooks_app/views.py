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
        'user': User.objects.get(id=request.session['id']),
        "books": Book.objects.all()

    }
    return render(request, 'books.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')


def home(request):
    return redirect('/books')

def add_book(request): 
    errors = Book.objects.validate_add_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        models.add_book(request)
        return redirect("/books")

def view_book(request, id):
    book = Book.objects.get(id=id)
    user_id = book.uploaded_by.id

    if user_id == request.session['id']:
        context = {
        "book": book,
        "user": User.objects.get(id=request.session['id']),
        "all_book": Book.objects.all(),
        }
        return render(request, 'edit_book.html', context)

    else:
        context = {
        "book": Book.objects.get(id=id),
        "user": User.objects.get(id=request.session['id']),
        "all_book": Book.objects.all(),
        }
        return render(request, 'view_book.html', context)

def edit_book(request, id):
    errors = Book.objects.validate_edit_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('f/books/{id}')
    else:
        book = Book.objects.get(id=id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
        return redirect('/books')



def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/books")


def add_to_favorites(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.liked_books.add(book)
    user.save()
    return redirect(f'/books/{id}')

def remove_from_favorites(request, id):
    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.liked_books.remove(book)
    user.save()
    return redirect(f'/books/{id}')

