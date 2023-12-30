from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.db.models import Count

import random 
from .models import Producto, Category
from .forms import NombreForm

# Create your views here.

def index(request):
     
     Productos = Producto.objects.all()
     Cantidad = Producto.objects.all().count()
     ProducosNew = Producto.objects.all()[:4]
     
     Categorys = []
     Cates = Producto.objects.values('Category').annotate(count = Count('Category'))
    
     for Cat in Cates:
          
          aux = Category(Cate = Cat.get('Category'), Cant = Cat.get('count'))
          Categorys.append(aux)    
    
     Categorys.reverse()
    
     Categorysc = len(Cates)
     #Cates = Producto.objects.aggregate(CateCount = Count('Category')) 
     #Categorysc = len(Cates)
     
     ListT = []
     

     for auc in Categorys:
          c = auc.Cate
          aux = Producto.objects.filter(Category = c)[:4]
          if aux:
               for e in aux:
                   ListT.append(e)
     
     
     
     Rebajas = Producto.objects.exclude(rebaja = 0)    
     rand = random.choice(Rebajas)
     rebaja = rand.Precio -(rand.Precio * rand.rebaja)/100
     rebaja = int(rebaja)
     
     print(Cates[0].get('Category')) 
          
     return render(request, 'index.html',context={'Productos':Productos, 'Cantidad':Cantidad,'Categorys':Categorys, 
                                                  'Categorysc':Categorysc, 'ProductosNew':ProducosNew,
                                                  'ListT': ListT, 'random':rand, 'rebaja':rebaja,'Cates':Cates,})
     
     
def Productos(request):
     
     Productos = Producto.objects.all()
     
     contenido = { 'Prod':Productos}
     
     return render(request, 'Productos.html', contenido)


def BuscarArticle(request):
     
     Buscar = request.GET.get("buscar")
     
     if Buscar == "":
          Productos = Producto.objects.all()
          
     else:
          Productos = Producto.objects.filter(Nombre__icontains = Buscar)
     
     constenido = {'Prod':Productos}
     
     return render(request,'Productos.html', constenido)


def SelectCate(request):
     
     Select = request.GET.get("Cat")
     
     print(Select)
     
     Productos = Producto.objects.filter(Category = Select)
     
     contenido = {'Prod':Productos}
     
     return render(request, 'Productos.html', contenido)