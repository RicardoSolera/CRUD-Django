#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import maquina

class maquinaForm(forms.ModelForm):

	Placa = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese la placa de la maquina'}))
	Estado = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el estado'}))
	Descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese una descripcion'}))
	
	class Meta:
		model = maquina
		fields = ['id_maquina','Placa','Estado', 'Descripcion']