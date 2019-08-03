from django import forms

from apps.catalogos.estado.models import Estado
from apps.catalogos.municipio.models import Municipio

estados = Estado.objects.filter(status=True)

class MunicipioForm(forms.ModelForm):
	class Meta:
		model = Municipio
		fields = [
			'estado',
			'nom_corto',
			'municipio'
		]
		labels = {
			'estado': 'Estado',
			'nom_corto': 'Nombre corto',
			'municipio': 'Municipio'
		}
		widgets = {
			'estado': forms.Select(attrs={'class':'form-control'}, choices=estados),			
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'municipio': forms.Select(attrs={'class':'form-control', 'required':True})
		}