from django.urls import path

from . import views
from .views import Productos, index
from .views import BuscarArticle, SelectCate, ProdSelect

urlpatterns = [
    path("", views.index, name="index"),
    path("Productos/", Productos, name="Productos"),
    path("index/", index, name = "Principal"),
    path("Prod/", BuscarArticle, name = "Buscar"),
    path("Cat/", SelectCate, name = "Categoria"),
    path("ProdSe/", ProdSelect, name = "Producto"),
]