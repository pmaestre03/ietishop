from django.urls import path
from . import views

urlpatterns = [
    path("", views.category_list, name="category_list"),
    path("/api/products/", views.product_list, name="product_list"),
    path("cat/<str:cat_name>/", views.product_list, name="product_list"),
    path ("prod/<str:product_name>/", views.detall_producte, name="detall_producte")
]