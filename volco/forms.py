#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import volco

class volcoForm(forms.ModelForm):

	Placa = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese la placa del Volvo'}))
	Chofer = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Ingrese el nombre del chofer'}))
	
	class Meta:
		model = volco
		fields = ['id_volco','Placa','Chofer']