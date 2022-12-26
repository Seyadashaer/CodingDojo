from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path("register", views.register),
    path("books", views.books),
    path("logout", views.logout),
    path("add", views.add),
    path("add_book", views.add_book),
    path("books/<int:id>", views.view_book),
    path("users/<int:id>", views.view_user),
    path("home", views.home),
    path("add_review", views.add_review)

]
