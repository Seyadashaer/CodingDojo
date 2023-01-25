from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_home),
    path('add_new_book', views.add_new_book),
    path('books/<int:book_id>', views.view_book),
    path('add_author_to_book/<int:book_id>', views.add_author_to_book),
    path('authors', views.authors_home),
    path('add_new_author', views.add_new_author),
    path('authors/<int:author_id>', views.view_author),
    path('add_book_to_author/<int:author_id>', views.add_book_to_author),
]