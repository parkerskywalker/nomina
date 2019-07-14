from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.catalogos.pais.views import index, PaisList, PaisCreate, PaisUpdate, PaisDelete

urlpatterns = [
    path('index', index, name='index'),
    
    path('list_pais', PaisList.as_view(), name='list_pais'),
    path('alta_pais', PaisCreate.as_view(), name='alta_pais'),
    path('edit_pais/<int:pk>/', PaisUpdate.as_view(), name='edit_pais'),
    path('delete_pais/<int:pk>/', PaisDelete.as_view(), name='delete_pais'),
]