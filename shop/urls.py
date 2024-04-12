from django.urls import path
from . import views, api

urlpatterns = [
    path("", views.product_list, name="category_list"),
    path("api/products/", api.getProducts, name="product_list"),
    path("api/products/<int:id_cat>/", api.getProductsByCategory, name="product_list"),
    path("cat/<str:cat_name>/", views.product_list, name="product_list"),
    path ("prod/<str:product_name>/", views.detall_producte, name="detall_producte"),
    path("cistella/", views.cistella, name="cistella"),
    path("api/cistella_products/<int:id_prod>/", api.getProductsById, name="product_list"),
]