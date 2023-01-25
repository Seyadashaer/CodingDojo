from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog Network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Show Description should be at least 10 characters"
            
        return errors

        
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    description = models.TextField(null=True)
    release_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()


def add_show(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    description = request.POST['description']

    Show.objects.create(title=title, network= network, release_date=release_date, description=description)


def get_all_shows():
    return Show.objects.all()

def get_show(id):
    return Show.objects.get(id=id)

def submit_edit(request, id):
    show = get_show(id=id)
    if request.POST['title']:
        show.title = request.POST['title']
    if request.POST['network']:
        show.network = request.POST['network']
    if request.POST['release_date']:
        show.release_date = request.POST['release_date']
    if request.POST['description']:
        show.description = request.POST['description']
    show.save()



