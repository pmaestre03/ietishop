from django.shortcuts import render
from .models import *

def category_list(request):
    categories = Categoria.objects.all()
    return render(request, "categories_list.html", {"categories": categories})

def product_list(request, cat_name=None):
    categories = Categoria.objects.all()
    if cat_name:
        categoria = Categoria.objects.get(nom=cat_name)
        productes = Producte.objects.filter(categoria=categoria)
    else:
        productes = Producte.objects.all()
    return render(request, "product_list.html", {"productes": productes, "categories": categories})

def detall_producte(request, product_name):
    producte = Producte.objects.get(nom=product_name)
    return render(request, "product_details.html", {"producte": producte})

def cistella(request):
    return render(request, "cistella.html")