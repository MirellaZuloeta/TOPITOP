from django.shortcuts import render, get_object_or_404
from .models import Producto
from category.models import Categoria


# Create your views here.

def tienda(request, categoria_slug=None):
    categorias = None
    productos = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        productos = Producto.objects.filter(categoria=categorias, disponible=True)

        contador = productos.count()
    else:
        productos = Producto.objects.all().filter(disponible=True)
        contador = productos.count()

    context = {
        'productos': productos,
        'contador': contador,
    }
    return render(request, 'tienda/tienda.html', context)



def detalle_producto(request, categoria_slug, producto_slug):
    try:
        single_product = Producto.objects.get(categoria__slug=categoria_slug, slug=producto_slug)
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
    }
    return render(request, 'tienda/detalle_producto.html', context)