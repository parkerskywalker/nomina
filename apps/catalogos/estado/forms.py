from django import forms

from apps.catalogos.pais.models import Pais
from apps.catalogos.estado.models import Estado


paises = Pais.objects.filter(status=True)

class EstadoForm(forms.ModelForm):

	"""
	def __init__(self, request, *args, **kwargs):
		super(EstadoForm, self).__init__(*args, **kwargs)
		self.fields['pais'].queryset=Pais.objects.filter(status=True)
	"""

	class Meta:
		model = Estado
		fields = [
			'pais',
			'nom_corto',
			'estado'
		]
		labels = {
			'pais': 'Pais',
			'nom_corto': 'Nombre corto',
			'estado': 'Estado'
		}
		widgets = {			
			'pais': forms.Select(attrs={'class':'form-control'}, choices=paises),			
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'estado': forms.Select(attrs={'class':'form-control', 'required':True})
		}
