from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.catalogos.municipio.forms import MunicipioForm
from apps.catalogos.municipio.models import Municipio

# Create your views here.
def index(request):
	return HttpResponse("Municipios")


class MunicipioList(ListView):
	model = Municipio
	template_name = 'catalogos/municipio/municipio_list.html'

class MunicipioCreate(CreateView):
	model = Municipio
	form_class = MunicipioForm
	template_name = 'catalogos/municipio/municipio_form.html'
	success_url = reverse_lazy('list_municipio')
