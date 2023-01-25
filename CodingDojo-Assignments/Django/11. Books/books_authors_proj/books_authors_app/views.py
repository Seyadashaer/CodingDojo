from django.shortcuts import render, redirect
from . import models

def books_home(request):
    context = {
        "all_books": models.get_all_books(),
        "all_authors": models.get_all_authors()
        }
    return render(request, 'books_home.html', context)

def authors_home(request):
    context = {
        "all_books": models.get_all_books(),
        "all_authors": models.get_all_authors()
        }
    return render(request, 'authors_home.html', context)

def view_book(request,book_id):
    context = {
        "all_books": models.get_all_books(),
        "all_authors": models.get_all_authors(),
        "book_id": models.get_book_id(book_id)
        }
    return render(request, 'view_book.html', context, book_id)

def view_author(request,author_id):
    context = {
        "all_books": models.get_all_books(),
        "all_authors": models.get_all_authors(),
        "author_id": models.get_author_id(author_id)
        }
    return render(request, 'view_author.html', context, author_id)

def add_new_book(request):
    models.add_new_book(request)
    return redirect('/')

def add_new_author(request):
    models.add_new_author(request)
    return redirect('/authors')

def add_author_to_book(request, book_id):
    models.add_author_to_book(request, book_id)
    return redirect(f'/books/{book_id}')

def add_book_to_author(request, author_id):
    models.add_book_to_author(request, author_id)
    return redirect(f'/authors/{author_id}')
