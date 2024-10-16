from django.db import models
from django.utils import timezone

class Book(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    valoracion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'