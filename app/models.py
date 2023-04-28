from django.db import models
from django.urls import reverse


class Book(models.Model):
    """
    Book model to store Books data
    """
    name_of_book = models.CharField(max_length=20)
    book_price = models.CharField(max_length=20)
    authors_name = models.CharField(max_length=20)
    author_phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name_of_book

    class Meta:
        """
        Meta class for Book Model
        """
        db_table = 'Books'

    def get_absolute_url(self):
        return reverse('update', args=[str(self.pk)])
