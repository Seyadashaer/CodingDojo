from django.db import models
import bcrypt
import re


NAME_REGEX = re.compile(r'[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'[a-zA-Z0-9.+_-]+@[a-zA_Z0-9._-]+\.[a-zA-z]+$')

class UserManager(models.Manager):
    def validate_register(self, postData):
        errors = {}

        if not postData['first_name']:
            errors['first_name'] = "First name is required"
        elif len(postData['first_name']) < 3:
            errors['first_name'] = "First name should be at least 3 characters"
        elif not NAME_REGEX.match(postData['first_name']):
            errors['first_name'] = "First Name should contain letters only"

        if not postData['last_name']:
            errors['last_name'] = "Last name is required"
        elif len(postData['last_name']) < 3:
            errors['last_name'] = "Last name should be at least 3 characters"
        elif not NAME_REGEX.match(postData['last_name']):
            errors['last_name'] = "Last name should contain letters only"

        if not postData['email']:
            errors['email'] = "Email is required"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email format"
        elif len(User.objects.filter(email = postData['email'])) > 0:
            errors['email'] = "Email already registered"

        if not postData['password']:
            errors['password'] = "Password is required"
        elif len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"

        if not postData['pw_confirm']:
            errors['pw_confirm'] = "Password confirmation is required"
        elif postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Passwords do not match"

        return errors


    def validate_login(self, postData):
        errors = {}

        if not postData['email']:
            errors['email'] = "Email is required"
        elif len(User.objects.filter(email = postData['email'])):
            user = User.objects.get(email = postData['email'])
            if not postData['password']:
                errors['password'] = "Password is required"
            elif not bcrypt.checkpw(postData['password'].encode(), user.password):
                errors['login'] = "Email OR Password incorrect"
        else:
            errors['login'] = "Email OR Password incorrect"

        return errors





class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.BinaryField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # voted_pies = a list of pies a given user votes
    # pies_added = a list of pies added by a given user


def get_current_user(request):
    return User.objects.get(id=request.session['id'])


class PieManager(models.Manager):
    def validate_pie(self, postData):
        errors = {}
        if len(postData['pie_name']) < 1:
            errors['pie_name'] = "The Pie name is required"
        if len(postData['filling']) < 1 :
            errors['filling'] = "Pie Filling is required"
        if len(postData['crust']) < 1 :
            errors['crust'] = "Pie Crust is required"
        return errors

class Pie(models.Model):
    pie_name = models.CharField(max_length=255)
    filling = models.CharField(max_length=255)
    crust = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, related_name="pies_added", on_delete=models.CASCADE)
    #  the user who added a given pie
    users_who_vote = models.ManyToManyField(User, related_name="voted_pies") 
    users_who_vote2 = models.ManyToManyField(User, related_name="voted_pies2")


    # a list of users who vote a given pie
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PieManager()


def add_pie(request):  
    pie_name = request.POST['pie_name']
    filling = request.POST['filling']
    crust = request.POST['crust']
    added_by = get_current_user(request)
    

    Pie.objects.create(pie_name=pie_name, filling=filling, crust=crust, added_by=added_by)

def get_pie(id):
    return Pie.objects.get(id=id)

def get_user_pies(request): 
    user = get_current_user(request)
    return Pie.objects.filter(added_by = user)


def add_vote(request, id):
    pie = get_pie(id=id)
    user = User.objects.get(id=request.session['id'])
    user.voted_pies.add(pie)
    user.voted_pies2.add(pie)
    pie.votes += 1
    pie.save()
    user.save()

def remove_vote(request, id):
    pie = get_pie(id=id)
    user = User.objects.get(id=request.session['id'])
    user.voted_pies.remove(pie)
    pie.votes -= 1
    pie.save()
    user.save()



def edit_pie(request, id):
    pie = get_pie(id=id)
    pie.pie_name = request.POST['pie_name']
    pie.filling = request.POST['filling']
    pie.crust = request.POST['crust']
    pie.save()


def get_all_pies():
    return Pie.objects.all()