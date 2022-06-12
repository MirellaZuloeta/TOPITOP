from django.contrib import admin
from .models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria', 'fecha_modificacion', 'disponible')
    prepopulated_fields = {'slug': ('nombre',)}


admin.site.register(Producto, ProductoAdmin)