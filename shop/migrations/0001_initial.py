# Generated by Django 4.2 on 2024-04-04 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descripcio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_compra', models.DateTimeField(auto_now_add=True)),
                ('preu_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('descripcio', models.TextField()),
                ('preu', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantitat_disponible', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categoria')),
                ('tags', models.ManyToManyField(to='shop.tag')),
            ],
        ),
        migrations.CreateModel(
            name='DetallCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitat', models.IntegerField(default=1)),
                ('preu_unitari', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.compra')),
                ('producte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.producte')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='productes',
            field=models.ManyToManyField(through='shop.DetallCompra', to='shop.producte'),
        ),
        migrations.AddField(
            model_name='compra',
            name='usuari',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cistella',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantitat', models.IntegerField(default=1)),
                ('producte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.producte')),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
