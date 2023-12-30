from django.contrib import admin
from .models import Producto, Category

# Register your models here.

admin.site.register(Producto)
admin.site.register(Category)