from __future__ import unicode_literals

from django.db import models

# Create your models here.

class volco(models.Model):
	"""docstring for volco"""


	id_volco=models.AutoField(primary_key=True)
	Placa=models.CharField(max_length=50)
	Chofer=models.CharField(max_length=100)

	def __str__(self):
 		return self.id_volco	

