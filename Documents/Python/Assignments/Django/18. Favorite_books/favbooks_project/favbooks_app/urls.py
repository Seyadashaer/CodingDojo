from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path("register", views.register),
    path("books", views.books),
    path("logout", views.logout),
    path("home", views.home),
    path("add_book", views.add_book),
    path("books/<int:id>", views.view_book), 
    path("edit_book/<int:id>", views.edit_book ),
    path("delete_book/<int:id>", views.delete_book),
    path("remove_from_favorites/<int:id>", views.remove_from_favorites),
    path("add_to_favorites/<int:id>", views.add_to_favorites)
]
