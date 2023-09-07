from django.utils import timezone
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Book, Books_rental

# Create your views here.

def HomePage(request):
    latest_books = Book.objects.all().order_by('-created')[:10]
    like_books = Book.objects.all().order_by('like')[:10]
    return render(request, 'home.html',{'latest_books':latest_books,'like_books':like_books})

class BooksList(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    redirect_field_name = 'accounts/login'
    
    paginate_by = 10
    
class BookDetail(generic.DetailView):
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
            Books_rental.objects.create(user=request.user,book=book,rental_date=timezone.localdate(),return_date=timezone.localdate()+timezone.timedelta(weeks=1))
            book.stock -= 1
            book.like += 1
            book.save()
            return redirect('books:my_rentals')
        else:
            raise ValueError('대여 불가능')

@login_required
def BookReturn(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        rental_book = get_object_or_404(Books_rental, book=book, user=request.user)
        book.stock += 1
        rental_book.book_return = True
        book.save()
        rental_book.save()
        return redirect('books:books_list')

@login_required
def BookReturnList(request):
    if request.user.is_superuser:
        rental_books = Books_rental.objects.filter(book_return=True)
        not_rental_books = Books_rental.objects.filter(book_return=False)
        return render(request, 'books/return_list.html', {'rental_books':rental_books,'not_rental_books':not_rental_books})
    else:
        return redirect('books:books_list')

def BookSearch(request):
    if request.method == 'POST':
        word = request.POST['word']
        books = Book.objects.filter(Q(title__icontains=word)|Q(author__icontains=word))
        
        return render(request,'books/books_list.html', {'books' : books})
    
    