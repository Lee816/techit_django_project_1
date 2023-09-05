from django.shortcuts import render
from django.views import generic

from .models import Book, Books_rental
# Create your views here.

class BooksList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'