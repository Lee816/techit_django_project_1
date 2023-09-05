from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render , get_object_or_404
from django.views import generic

from .models import Book, Books_rental
# Create your views here.

class BooksList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    
class BookDetail(generic.DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    
class RentalBooksList(generic.ListView):
    model = Books_rental
    context_object_name = 'rental_books'
    template_name = 'books/rental_list.html'
    
    def get_queryset(self):
        return Books_rental.objects.filter(user=self.request.user)