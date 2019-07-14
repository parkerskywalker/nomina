from django.db import models
from datetime import datetime

class Pais(models.Model):
	nom_corto = models.CharField(max_length=3, null=False, unique=True, default='')
	pais = models.CharField(max_length=30, null=False, default='')
	usuario = models.IntegerField(default=0)
	fecha = models.DateTimeField(default=datetime.now())
	status = models.BooleanField(default=True)

	def __str__(self):
		return '{} {}'.format(self.nom_corto, self.pais)
