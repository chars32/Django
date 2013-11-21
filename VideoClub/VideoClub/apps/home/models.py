from django.db import models

class Actor(models.Model):
	nombre = models.CharField(max_length=100)
	nacimiento = models.DateField()

	def __unicode__(self):
		return self.nombre

class Pelicula(models.Model):
	nombre = models.CharField(max_length=100)
	anio = models.IntegerField()
	actores = models.ManyToManyField(Actor, related_name='peliculas')

	def __unicode__(self):
		return self.nombre