from django.contrib import admin
from django.urls import path, include

from django.config import settings
from django.config.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('catalogos/pais/', include('apps.catalogos.pais.urls')),
    path('catalogos/estado/', include('apps.catalogos.estado.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)