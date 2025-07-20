from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=200,validators=[MinLengthValidator(2),MaxLengthValidator(50)])

    def __str__(self):
        return self.name

        
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,validators=[MinLengthValidator(10), MaxLengthValidator(50)])
    desc = models.CharField(max_length=400)
    rate = models.DecimalField(max_digits=2,decimal_places=1)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book')
    category = models.ManyToManyField(Category,related_name='books')


    def __str__(self):
        return self.title





class ISBN(models.Model):
    ISBN_number=models.CharField(max_length=50 ,primary_key=True)
    book=models.OneToOneField(Book,on_delete=models.CASCADE, related_name='ISBN')
    
    def __str__(self):
        return self.ISBN_number


