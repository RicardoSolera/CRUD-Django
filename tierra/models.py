from __future__ import unicode_literals

from django.db import models

# Create your models here.
class  tierra(models.Model):
	"""docstring for  tierra"""
	id_tierra=models.AutoField(primary_key=True)
	Nombre=models.CharField(max_length=50)
	Descripcion=models.CharField(max_length=100)
	Precio=models.CharField(max_length=50)

	#def __init__(self, arg):
	#	super( tierra, self).__init__()
	#	self.arg = arg
	def __str__(self):
		return self.id_tierra
		