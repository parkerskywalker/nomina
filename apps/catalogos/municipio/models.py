from django.db import models
from apps.catalogos.estado.models import Estado

from datetime import datetime

class Municipio(models.Model):
	nom_corto = models.CharField(max_length=3, null=False, unique=True, default='')
	estado = models.ForeignKey(Estado, default='', null=False, blank=False, on_delete=models.PROTECT)
	municipio= models.CharField(max_length=30, null=False, blank=True, unique=True)
	usuario = models.IntegerField(default=0)
	fecha = models.DateTimeField(default=datetime.now())
	status = models.BooleanField(default=True)

	def __str__(self):
		return '{}'.format(self.municipio)