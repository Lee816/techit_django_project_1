from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('list/', views.BooksList.as_view(), name='books_list'),
    path('rental_list/', views.RentalBooksList.as_view(), name='rental_list'),
    path('<int:book_id>/detail/', views.BookDetail.as_view(), name='book_detail'),
]
