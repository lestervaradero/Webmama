from django.db import models

# Create your models here.

class Producto(models.Model):
    Nombre = models.CharField(max_length=300)
    Category = models.CharField(max_length=300)
    Precio = models.IntegerField()
    rebaja = models.IntegerField()
    new = models.BooleanField()
    Timage = models.ImageField(upload_to= 'Productos', null=True)
    Descripcion = models.TextField(null = True)
    
    
    
class Category(models.Model):
    Cate = models.CharField(max_length=300)
    Cant = models.IntegerField()
    
   