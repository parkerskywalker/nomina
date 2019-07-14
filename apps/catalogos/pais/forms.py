from django import forms

from apps.catalogos.pais.models import Pais

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = [
            'nom_corto',
            'pais'
        ]
        labels = {
            'nom_corto': 'Nombre corto',
            'pais': 'Pais'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'pais':forms.TextInput(attrs={'class':'form-control', 'required':True}),            
        }