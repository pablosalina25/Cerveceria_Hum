# Generated by Django 4.2.5 on 2024-09-06 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('sitio_web', models.URLField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Fabricantes',
            },
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(blank=True)),
                ('tamaño', models.PositiveIntegerField(help_text='En mililitros')),
            ],
        ),
        migrations.CreateModel(
            name='Cerveza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('variedad', models.CharField(max_length=60)),
                ('estilo', models.CharField(max_length=60)),
                ('volumen_de_alcohol', models.DecimalField(decimal_places=2, max_digits=10)),
                ('origen', models.CharField(max_length=60)),
                ('fecha_elaboracion', models.DateField()),
                ('portada', models.ImageField(upload_to='portadas')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.TextField(blank=True)),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cerveceria.fabricante')),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cerveceria.presentacion')),
            ],
            options={
                'verbose_name_plural': 'Cervezas',
            },
        ),
    ]
