from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(unique=True, max_length=13)
    available_copies = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# BorrowRecord model
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, related_name='borrow_records', on_delete=models.CASCADE)
    borrowed_by = models.CharField(max_length=255)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} borrowed by {self.borrowed_by}'

