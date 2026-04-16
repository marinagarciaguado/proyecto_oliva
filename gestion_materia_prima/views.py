from django.shortcuts import render, get_object_or_404
from .models import LoteMateriaPrima

# Vista para el listado general de lotes (Tarea 5.a)
def lista_lotes(request):
    # Obtenemos todos los lotes guardados en la base de datos
    lotes = LoteMateriaPrima.objects.all() 
    # Enviamos los lotes al archivo HTML 'lista_lotes.html'
    return render(request, 'gestion_materia_prima/lista_lotes.html', {'lotes': lotes})

# Vista para ver el detalle de un lote específico (Tarea 5.b)
def detalle_lote(request, lote_id):
    # Buscamos el lote por su ID. Si no existe, lanza un error 404.
    lote = get_object_or_404(LoteMateriaPrima, pk=lote_id)
    # Enviamos la información al archivo HTML 'detalle_lote.html'
    return render(request, 'gestion_materia_prima/detalle_lote.html', {'lote': lote})