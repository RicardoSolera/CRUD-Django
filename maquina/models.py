from __future__ import unicode_literals

from django.db import models

# Create your models here.

class maquina(models.Model):
	"""docstring for maquina"""
	id_maquina=models.AutoField(primary_key=True)
	Placa=models.CharField(max_length=50)
	Estado=models.CharField(max_length=100)
	Descripcion=models.CharField(max_length=100)

	def __str__(self):
 		return self.id_maquina
		


