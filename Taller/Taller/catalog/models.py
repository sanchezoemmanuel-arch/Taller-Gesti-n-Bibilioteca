from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
        
    def __str__(self): 
        return f"{self.first_name}, {self.last_name}"




class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título") 
    summary = models.TextField(max_length=1000, verbose_name="Resumen")
    author = models.CharField(max_length=200, null=True, blank=True, verbose_name="Autor")
    isbn = models.CharField(max_length=13, verbose_name="Código ISBN")
    is_available = models.BooleanField(default=True, verbose_name="¿Está disponible?")


    class Meta:
        verbose_name = "Libro"         
        verbose_name_plural = "Libros"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.author})"
