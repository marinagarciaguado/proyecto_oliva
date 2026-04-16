from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materia-prima/', include('gestion_materia_prima.urls')),
    path('produccion/', include('gestion_produccion.urls')), # Nueva línea [cite: 400]
]