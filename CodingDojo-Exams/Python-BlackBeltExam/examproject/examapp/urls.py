from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login", views.login),
    path("register", views.register),
    path("dashboard", views.dashboard),
    path("logout", views.logout),
    path("edit/<int:id>", views.edit_pie_page),
    path("delete/<int:id>", views.delete_pie),
    path("show/<int:id>", views.show_pie),
    path("pies", views.show_all_pies),
    path("add_pie", views.add_pie), 
    path("add_vote/<int:id>", views.add_vote),
    path("remove_vote/<int:id>", views.remove_vote),
    path("edit_pie/<int:id>", views.edit_pie)

]
