from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
class Experiencia(models.Model):
    nombre = models.CharField(max_length=100)
    listProyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,related_name='experiencia')
class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
class Lenguaje(models.Model):
    nombre = models.CharField(max_length=100)
    expirencia = models.IntegerField()
class Social(models.Model):
    nombre = models.CharField(max_length=100)
    url = models.URLField()
class Trabajo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fechaIni = models.DateField()
    fechaFin = models.DateField()
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=1)
    imagen = models.ImageField(upload_to='portfolio/')
    listHabilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE,related_name='usuario')
    listaLenguaje = models.ForeignKey(Lenguaje, on_delete=models.CASCADE,related_name='usuario')
    listaTrabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE,related_name='usuario')
    listaSocial = models.ForeignKey(Social, on_delete=models.CASCADE,related_name='usuario')
    listaProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,related_name='usuario')
    listaExperiencia = models.ForeignKey(Experiencia, on_delete=models.CASCADE,related_name='usuario')