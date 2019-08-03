from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.catalogos.municipio.views import index, MunicipioList, MunicipioCreate

urlpatterns = [
	#path('index', index, name='index'),

	path('list_municipio', MunicipioList.as_view(), name='list_municipio'),
    path('alta_municipio', MunicipioCreate.as_view(), name='alta_municipio'),
    #path('edit_municipio/<int:pk>/', MunicipioUpdate.as_view(), name='edit_municipio'),
    #path('delete_municipio/<int:pk>/', MunicipioDelete.as_view(), name='delete_municipio'),
] 