from django.db import models

# Create your models here.

class Fabricante(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    sitio_web = models.URLField(max_length=255)

    class Meta:
        verbose_name_plural = 'Fabricantes'

    def __str__(self):
        return self.nombre

# verbose es para generar el plural en el admin 

class Presentacion(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(blank=True)
    tamaño = models.PositiveIntegerField(help_text="En mililitros")

    def __str__(self):
        return self.nombre

class Cerveza(models.Model):
    nombre = models.CharField(max_length=100)
    variedad = models.CharField(max_length=60)
    estilo = models.CharField(max_length=60)
    volumen_de_alcohol = models.DecimalField(max_digits=10, decimal_places=2)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    origen = models.CharField(max_length=60)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    fecha_elaboracion = models.DateField()
    portada = models.ImageField(upload_to='portadas')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return "%s" % (self.nombre)

    class Meta:
        verbose_name_plural = 'Cervezas'
