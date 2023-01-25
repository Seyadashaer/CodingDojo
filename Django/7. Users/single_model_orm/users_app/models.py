from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_user(first_name, last_name, email_address, age ):
    User.objects.create(first_name =first_name, last_name = last_name, email_address = email_address, age = age)

def get_all_users(): 
    return User.objects.all()
