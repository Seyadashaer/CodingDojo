from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.index),
    path('add_course', views.add_course),
    path('display_delete_page/<int:id>', views.display_delete_page),
    path('delete_course/<int:id>', views.delete_course)
]