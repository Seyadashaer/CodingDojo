from django.db import models
import bcrypt
import re


EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')
NAME_REGEX = re.compile(r'[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}
        
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First name should only contain letters"

        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name should be at least 2 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['last_name'] = "Last name should only contain letters"

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "Email already registered"

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['password_confirm']:
            errors['password'] = "Password should match password confirmation"

        return errors

    def validate_login(self, postData):
        errors = {}
        if len(User.objects.filter(email = postData['email'])):
            user = User.objects.get(email = postData['email'])
            if bcrypt.checkpw(postData['password'].encode(), user.password):
                return errors
            else:
                errors['login'] = "Email/password incorrect"
                return errors
        else:
            errors['login'] = "Email/password incorrect"
            return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()