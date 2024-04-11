from django.contrib import admin
from .models import *

admin.site.register(Tag)
admin.site.register(Producte)

admin.site.register(Cistella)

class CompraInline(admin.TabularInline):
    model = Compra
    extra = 0

class DetallCompraInline(admin.TabularInline):
    model = DetallCompra
    extra = 0
    readonly_fields = ["preu_unitari"]

class DetallCompraAdmin(admin.ModelAdmin):
    model = DetallCompra
    extra = 0
    readonly_fields = ["preu_unitari"]

class ProducteInline(admin.TabularInline):
    model = Producte
    readonly_fields = ["descripcio"]

class CategoriaInline(admin.TabularInline):
    model = Categoria
    extra = 0
    exclude = ("descripcio",)

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaInline, ProducteInline]
    list_display = ["nom","parent"]

class CompraAdmin(admin.ModelAdmin):
    inlines = [DetallCompraInline]
    list_display = ['usuari', 'data_compra', 'preu_total']

class CistellaAdmin(admin.ModelAdmin):
    inlines = [CompraInline]
    readonly_fields = ["preu_total"]

admin.site.register(DetallCompra, DetallCompraAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Compra, CompraAdmin)
