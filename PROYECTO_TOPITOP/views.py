from django.shortcuts import render
from tienda.models import Producto

def home(request):
    productos = Producto.objects.all().filter(disponible=True).order_by('fecha_creacion')

    context = {
        'productos': productos,
    }
    return render(request, 'home.html', context)