from django.urls import path
from .views import (
    HomeView, BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView,
    CurrentTimeView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/add/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:id>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:id>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('time/', CurrentTimeView.as_view(), name='current_time'),
]
