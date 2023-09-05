from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Book, Books_rental

# Create your views here.

class BooksList(LoginRequiredMixin, generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    redirect_field_name = 'accounts/login'
    
class BookDetail(LoginRequiredMixin, generic.DetailView):
    model = Book
    pk_url_kwarg = 'book_id'
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    redirect_field_name = 'accounts/login'
    
class BookCreate(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = Book
    fields = '__all__'
    context_object_name = 'form'
    redirect_field_name = 'accounts:login'
    template_name = 'books/book_create.html'
    permission_required = 'books.add_book'
    success_url = reverse_lazy('books:books_list')
    
class RentalBooksList(LoginRequiredMixin, generic.ListView):
    model = Books_rental
    context_object_name = 'rental_books'
    template_name = 'books/rental_list.html'
    redirect_field_name = 'accounts/login'
    
    def get_queryset(self):
        return Books_rental.objects.filter(user=self.request.user)

@login_required
def BookRent(request, book_id):
    if request.user.is_anonymous :
        return redirect('accounts:login')
    else:
        book = get_object_or_404(Book, id=book_id)
        if book.stock > 0 :
            Books_rental.objects.create(user=request.user,book=book)
            book.stock -= 1
            book.save()
            return redirect('books:books_list')
        else:
            raise ValueError('대여 불가능')

@login_required
@permission_required('books.delete_Books_rental')
def BookReturn(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        rental_book = get_object_or_404(Books_rental, book=book, user=request.user)
        book.stock += 1
        rental_book.delete()
        return redirect('books:books_list')

@login_required
def BookReturnList(request):
    rental_books = Books_rental.objects.filter(book_return=True)
    return render(request, 'books/return_list.html', {'rental_books':rental_books})
    