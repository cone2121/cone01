from django.db import models

# Create your models here.
class Libros(models.Model):
    nombre = models.CharField(max_length=200)
    isbn=models.CharField(max_length=60)
    autor=models.CharField(max_length=200)