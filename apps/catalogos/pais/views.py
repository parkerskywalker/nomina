from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from apps.catalogos.pais.forms import PaisForm
from apps.catalogos.pais.models import Pais

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo")

class PaisList(ListView):
	model = Pais
	template_name='catalogos/pais/pais_list.html'

class PaisCreate(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'catalogos/pais/pais_form.html'    
    success_url = reverse_lazy('list_pais')

class PaisUpdate(UpdateView):
	model = Pais
	form_class = PaisForm
	template_name = 'catalogos/pais/pais_form.html'
	success_url = reverse_lazy('list_pais')

class PaisDelete(DeleteView):
	model = Pais
	form_class = PaisForm
	template_name = 'catalogos/pais/pais_delete.html'
	success_url = reverse_lazy('list_pais')