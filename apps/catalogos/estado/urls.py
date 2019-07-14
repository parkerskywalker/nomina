from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.catalogos.estado.views import index, EstadoList, EstadoCreate, EstadoUpdate, EstadoDelete

urlpatterns = [
	path('index', index, name='index'),

	path('list_estado', EstadoList.as_view(), name='list_estado'),
    path('alta_estado', EstadoCreate.as_view(), name='alta_estado'),
    path('edit_estado/<int:pk>/', EstadoUpdate.as_view(), name='edit_estado'),
    path('delete_estado/<int:pk>/', EstadoDelete.as_view(), name='delete_estado'),
]