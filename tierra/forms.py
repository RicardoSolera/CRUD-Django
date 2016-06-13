#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import tierra

class tierraForm(forms.ModelForm):

	#id_tierra= forms.ModelChoiceField(queryset=tierra.objects.all(), initial=0, to_field_name="id_tierra")
	Nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el nombre de la tierra'}))
	Descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese breve descripcion'}))
	Precio = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el precio venta'}))

	class Meta:
		model = tierra
		fields = ['id_tierra','Nombre','Descripcion','Precio']