from django.db import models
from django.utils import timezone, dates

from accounts.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='books',on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    summary = models.TextField()
    like = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Books_rental(models.Model):
    rental_date = models.DateField(default=timezone.now())
    return_date = models.DateField(default=timezone.now()+timezone.timedelta(weeks=1))
    book = models.ForeignKey(Book, related_name='rentals', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='rental_books', on_delete=models.CASCADE)
    book_return = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} rental "{self.book}"'