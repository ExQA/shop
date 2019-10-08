from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('calculator/', views.calc),
    path('examples/', views.examples),
    path('book-info/<int:id>', views.book_info),
    path('all-books-for-author/<int:id_author>', views.all_books_for_author),
]
# url(r'^about$')
