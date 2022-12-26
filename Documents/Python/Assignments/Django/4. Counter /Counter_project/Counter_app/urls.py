from django.urls import path     
from . import views

urlpatterns = [
    path('', views.count),
    path('destroy_session', views.destroy_session),
    path('add_two', views.add_two)
]
