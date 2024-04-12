from django.http import JsonResponse
from .models import *
 
def getProducts(request):
    jsonData = list( Producte.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "productes": jsonData,
        }, safe=False)

def getProductsByCategory(request, id_cat):
    jsonData = list( Producte.objects.filter(categoria=id_cat).values() )
    return JsonResponse({
            "status": "OK",
            "productes": jsonData,
        }, safe=False)

def getCategories(request):
    jsonData = list( Categoria.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "categories": jsonData,
        }, safe=False)

def getProductsById(request, id_prod):
    jsonData = list( Producte.objects.filter(id=id_prod).values() )
    return JsonResponse({
            "status": "OK",
            "productes": jsonData,
        }, safe=False)