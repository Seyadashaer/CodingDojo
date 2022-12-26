from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField(null = True)

def get_all_books(): 
    return Book.objects.all()

def get_all_authors():
    return Author.objects.all()

def get_book_id(book_id): 
    return Book.objects.get(id=book_id)

def get_author_id(author_id):
    return Author.objects.get(id=author_id)

def add_new_book(request):
    new_book_title = request.POST['book_title']
    new_book_description = request.POST['book_description']
    Book.objects.create(title=new_book_title, description=new_book_description)

def add_new_author(request):
    new_author_first = request.POST['author_first_name']
    new_author_last = request.POST['author_last_name']
    new_author_notes = request.POST['author_notes']
    Author.objects.create(first_name=new_author_first, last_name=new_author_last, notes=new_author_notes)


def add_author_to_book(request, book_id):
    author_id = request.POST['author_dropdown']
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=book_id)
    book.authors.add(author)

def add_book_to_author(request, author_id):
    book_id = request.POST['book_dropdown']
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=author_id)
    author.books.add(book)