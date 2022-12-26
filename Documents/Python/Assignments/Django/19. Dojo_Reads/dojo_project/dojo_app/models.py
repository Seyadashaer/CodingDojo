from django.db import models
import bcrypt
import re

NAME_REGEX = re.compile(r'[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')

class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First Name should contain letters only"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name should contain letters only"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email = postData['email'])) > 0:
            errors['email'] = "Email already registered"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Passwords do not match"
        return errors


    def validate_login(self, postData):
        errors = {}
        if len(User.objects.filter(email = postData['email'])):
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['login'] = "Email OR Password incorrect"
                return errors
        else:
            errors['login'] = "Email OR Password incorrect"
            return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.BinaryField(max_length=255)
    pw_confirm = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    review = models.TextField()
    rating = models.SmallIntegerField(blank=True, null=True)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def add_book(request): 
    if len(request.POST['author']):
        author = Author.objects.create(author = request.POST['author'])
    else:
        author = Author.objects.get(id = request.POST['author_id'])
    title = request.POST['title']
    book = Book.objects.create(title=title, author=author)
    review = request.POST['review']
    rating = request.POST['rating']
    user = User.objects.get(id = request.session['id'])
    Review.objects.create(review=review, rating=rating, book= book, user = user)


def add_review(request):
    review = request.POST['review']
    rating = request.POST['rating']
    book = Book.objects.get(id = request.POST['book_id'])
    user = User.objects.get(id = request.session['id'])
    Review.objects.create(review=review, rating=rating, book=book, user=user)
