import uuid # Añade esta importación al principio
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
    
    lotes_materia_prima = models.ManyToManyField(LoteMateriaPrima)

    # --- AÑADE ESTO ---
    def save(self, *args, **kwargs):
        if not self.codigo_seguimiento:
            # Genera un código único corto, ej: PROD-1A2B3C
            self.codigo_seguimiento = f"PROD-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    # ------------------

    def __str__(self):
        return f"Producción #{self.codigo_seguimiento} ({self.estado})"