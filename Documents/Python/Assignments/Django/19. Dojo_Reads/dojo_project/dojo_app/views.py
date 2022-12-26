from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User , Book, Review, Author
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
        "books" : Book.objects.all(),
        'reviews': Review.objects.order_by('-created_at')[:3]
    }
    return render(request, 'books.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def add(request): 
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, "add.html", context)

def add_book(request): 
    models.add_book(request)
    return redirect('/books')

def view_book(request, id):
    book = Book.objects.get(id = id)
    context = {
        'book': book,
        'reviews': Review.objects.filter(book = book)
    }
    return render(request, "view_book.html", context)


def view_user(request, id):
    user = User.objects.get(id=id)
    context = { 
        "user": user,
        "reviews" : Review.objects.filter(user = user),
        'count': Review.objects.filter(user = user).count()
    }
    return render(request, "view_user.html", context)

def add_review(request):
    id = request.POST['book_id']
    models.add_review(request)
    return redirect(f'/books/{id}')

def home(request):
    return redirect('/books')
