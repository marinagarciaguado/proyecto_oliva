import uuid
from django.db import models
from gestion_usuarios.models import Productor # Importamos el Productor

class LoteMateriaPrima(models.Model):
    # Estados definidos en la práctica [cite: 18, 364]
    ESTADOS = [
        ('INGRESADO', 'Ingresado'),
        ('ANALISIS', 'En análisis'),
        ('ANALIZADO', 'Analizado'),
        ('ASIGNADO', 'Asignado a Lote de producción'),
    ]

    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    # Código de 24 dígitos 
    codigo = models.CharField(max_length=24, unique=True, editable=False)
    fecha_cosecha = models.DateField()
    fecha_arribo = models.DateTimeField(auto_now_add=True) # Se pone solo al crearse [cite: 10]
    
    # Pesaje [cite: 12]
    peso_bruto = models.FloatField()
    peso_tara = models.FloatField()
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default='INGRESADO')

    def save(self, *args, **kwargs):
        # Lógica para generar el código de 24 dígitos si no existe
        if not self.codigo:
            self.codigo = str(uuid.uuid4().int)[:24]
        super().save(*args, **kwargs)

    @property
    def peso_neto(self):
        # El reporte debe indicar el peso neto [cite: 122]
        return self.peso_bruto - self.peso_tara

    def __str__(self):
        return f"Lote {self.codigo} ({self.productor.nombre})"
    
class ResultadoAnalisis(models.Model):
    lote = models.ForeignKey(LoteMateriaPrima, on_delete=models.CASCADE, related_name='analisis')
    tipo_analisis = models.CharField(max_length=100) # Ej: "Madurez", "Defectos" [cite: 36, 42]
    fecha_hora = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Analisis {self.tipo_analisis} - Lote {self.lote.codigo}"