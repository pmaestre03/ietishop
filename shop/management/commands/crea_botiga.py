from django.core.management.base import BaseCommand
from faker import Faker
from faker_music import MusicProvider
from shop.models import Categoria, Producte
import random

class Command(BaseCommand):
    help = 'Crea categorías y productos de prueba relacionados con instrumentos musicales'

    def handle(self, *args, **kwargs):
        fake = Faker()
        fake.add_provider(MusicProvider)
        
        num_categorias = 100  # Definimos solo una categoría ya que los instrumentos se agrupan bajo una sola categoría
        num_productos_por_categoria = 10  # Número de productos relacionados con instrumentos por cada categoría

        self.crear_categorias_e_instrumentos(fake)
      
    def crear_categorias_e_instrumentos(self, fake):
        # Obtenemos los datos de instrumentos musicales del proveedor
        # Creamos una única categoría para los instrumentos musicales
        categories = 0
        while categories != 4:
         productos_y_categorias = fake.music_instrument_object()
         # Creamos la categoría solo si no existe ya con el mismo nombre
         categoria_nombre = productos_y_categorias['category']
         if not Categoria.objects.filter(nom=categoria_nombre).exists():
                  categoria = Categoria.objects.create(
                  nom=categoria_nombre,
                  descripcio=fake.paragraph()
                  )
                  self.stdout.write(self.style.SUCCESS(f'Categoría creada: {categoria.nom}'))
                  categories += 1
         else:
                  self.stdout.write(self.style.WARNING(f'La categoría "{categoria_nombre}" ya existe y no se creará de nuevo.'))

         categoria = Categoria.objects.get(nom=categoria_nombre)

         for producto_nombre in productos_y_categorias['instruments']:
                  # Creamos el producto solo si no existe ya con el mismo nombre
                  if not Producte.objects.filter(nom=producto_nombre).exists():
                   producto = Producte.objects.create(
                           nom=producto_nombre,
                           descripcio=fake.paragraph(),
                           preu=random.uniform(10, 1000),
                           categoria=categoria,
                           quantitat_disponible=random.randint(1, 100)
                   )
                   self.stdout.write(self.style.SUCCESS(f'Producto creado: {producto.nom}'))
                  else:
                   self.stdout.write(self.style.WARNING(f'El producto "{producto_nombre}" ya existe y no se creará de nuevo.'))