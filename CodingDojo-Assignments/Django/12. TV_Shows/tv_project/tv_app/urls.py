from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.index),
    path('add_show', views.add_show),
    path('shows', views.view_all_shows),
    path('shows/<int:id>', views.view_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/submit_edit', views.submit_edit),
    path('shows/<int:id>/delete', views.delete_show)
    
]