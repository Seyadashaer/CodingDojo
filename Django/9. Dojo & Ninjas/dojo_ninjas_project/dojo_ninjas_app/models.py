from django.db import models

class Dojo(models.Model): 
    name = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=2, null=True)
    desc = models.TextField(null=True)

class Ninja(models.Model): 
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    dojo = models.ForeignKey(Dojo, related_name='ninjas', on_delete=models.CASCADE)

def add_dojo(request): 
    name = request.POST['dojo_name']
    city = request.POST['dojo_city']
    state = request.POST['dojo_state']

    Dojo.objects.create(name=name, city=city, state=state)

def add_ninja(request): 
    my_dojo = Dojo.objects.get(id=request.POST['ninja_dojo'])
    first_name = request.POST['ninja_first_name']
    last_name = request.POST['ninja_last_name']

    Ninja.objects.create(dojo=my_dojo, first_name=first_name, last_name=last_name)

def get_all_dojos():
    return Dojo.objects.all()

def get_all_ninjas():
    return Ninja.objects.all()