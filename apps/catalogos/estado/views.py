from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.catalogos.estado.forms import EstadoForm
from apps.catalogos.estado.models import Estado

# Create your views here.
def index(request):
	return HttpResponse("Hola")

class EstadoList(ListView):
	model = Estado
	template_name='catalogos/estado/estado_list.html'

class EstadoCreate(CreateView):
	model = Estado
	form_class = EstadoForm
	template_name = 'catalogos/estado/estado_form.html'
	success_url = reverse_lazy('list_estado')

class EstadoUpdate(UpdateView):
	model = Estado
	form_class = EstadoForm
	template_name = 'catalogos/estado/estado_form.html'
	success_url = reverse_lazy('list_estado')

class EstadoDelete(DeleteView):
	model = Estado
	form_class = EstadoForm
	template_name = 'catalogos/estado/estado_delete.html'
	success_url = reverse_lazy('list_estado')

