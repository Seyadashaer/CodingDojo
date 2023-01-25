from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData): 
        errors = {}
        if len(postData['name']) <5:
            errors['name'] = "Course name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Course description should be at least 15 characters"
        return errors


class Course(models.Model): 
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

def get_all_courses():
    return Course.objects.all()

def add_course(request):
    name = request.POST['name']
    description = request.POST['description']

    Course.objects.create(name=name, description=description)

def get_course(id):
    return Course.objects.get(id=id)

def delete_course(id): 
    course = get_course(id=id)
    course.delete()