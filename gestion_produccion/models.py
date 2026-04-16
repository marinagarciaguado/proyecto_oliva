from django.db import models
from gestion_materia_prima.models import LoteMateriaPrima

class LoteProduccion(models.Model):
    ESTADOS = [
        ('ARMADO', 'En armado'),
        ('FINALIZADO', 'Finalizado'),
    ] 

    codigo_seguimiento = models.CharField(max_length=20, unique=True, editable=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='ARMADO')
    
    # Un lote de producción agrupa varios de materia prima 
    lotes_materia_prima = models.ManyToManyField(LoteMateriaPrima)

    def __str__(self):
        return f"Producción #{self.codigo_seguimiento} ({self.estado})"