from django.shortcuts import render, get_object_or_404
from .models import LoteProduccion

# Vista general de lotes de producción (Tarea 6.a)
def lista_produccion(request):
    # Obtenemos todos los lotes de producción de la base de datos 
    lotes_produccion = LoteProduccion.objects.all()
    return render(request, 'gestion_produccion/lista_produccion.html', {'lotes': lotes_produccion})

# Vista detalle de un lote de producción (Tarea 6.b)
def detalle_produccion(request, produccion_id):
    # Obtenemos el lote específico o error 404 [cite: 389]
    lote_p = get_object_or_404(LoteProduccion, pk=produccion_id)
    return render(request, 'gestion_produccion/detalle_produccion.html', {'lote_p': lote_p})