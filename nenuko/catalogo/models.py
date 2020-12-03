from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genero(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Marca(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Manga(models.Model):
    
	titulo = models.CharField(max_length=200)
	mangaka = models.ForeignKey('Mangaka', on_delete=models.SET_NULL, null=True)
    
	descripcion = models.TextField(max_length=1000)
	volumen = models.CharField('Volumen', max_length=13)
	genero = models.ManyToManyField(Genero)
    
	def __str__(self):
		return self.titulo
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this manga."""
		return reverse('manga-detail', args=[str(self.id)])
		
class Mangaka(models.Model):
	"""Model representing an Mangaka."""
	primer_nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField()
	fecha_muerte = models.DateField( null=True, blank=True)
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.primer_nombre}'	
class Figuras(models.Model):
    
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=1000)
	marca = models.ManyToManyField(Marca)
    
	def __str__(self):
		return self.titulo
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this manga."""
		return reverse('figuras-detail', args=[str(self.id)])
		