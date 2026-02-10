from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    genre = models.CharField(max_length=100, default='Fiction')
    created_by = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name




class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    num_pages = models.IntegerField()
    date_published = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
