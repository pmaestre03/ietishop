from django.contrib.auth.models import User
from django.db import models

class Categoria(models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.TextField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nom

class Tag(models.Model):
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom

class Producte(models.Model):
    nom = models.CharField(max_length=200)
    descripcio = models.TextField()
    preu = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    quantitat_disponible = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nom

class Cistella(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    productes = models.ManyToManyField(Producte, through='CistellaProducte')
    
    def __str__(self):
        return f"Cesta de {self.usuari.username}"
    
    class Meta:
        verbose_name_plural = "Cistelles"

class CistellaProducte(models.Model):
    cistella = models.ForeignKey(Cistella, on_delete=models.CASCADE)
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    quantitat = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.cistella} - {self.producte} - {self.quantitat}"

class Compra(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    productes = models.ManyToManyField(Producte, through='DetallCompra')
    data_compra = models.DateTimeField(auto_now_add=True)
    preu_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
         # Calcula el precio total de la compra antes de guardar
         self.preu_total = sum(detall.preu_unitari * detall.quantitat for detall in self.detallcompra_set.all())
         super().save(*args, **kwargs)
    
    def __str__(self):
         return f"Compra de {self.usuari.username} - {self.data_compra}"

class DetallCompra(models.Model):
    producte = models.ForeignKey(Producte, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    quantitat = models.IntegerField(default=1)
    preu_unitari = models.DecimalField(max_digits=10, decimal_places=2)  # Hacerlo de solo lectura
    
    def save(self, *args, **kwargs):
        # Calcula el precio unitario del producto antes de guardar
        self.preu_unitari = self.producte.preu
        super().save(*args, **kwargs)