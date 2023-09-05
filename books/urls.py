from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('list/', views.BooksList.as_view(), name='books_list'),
]
