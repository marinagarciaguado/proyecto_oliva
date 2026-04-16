from django.core.management.base import BaseCommand
from gestion_usuarios.models import Productor
from gestion_materia_prima.models import LoteMateriaPrima
from gestion_produccion.models import LoteProduccion
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Popula la base de datos con datos de prueba iniciales'

    def handle(self, *args, **options):
        self.stdout.write('Populando base de datos...')

        # 1. Crear un Productor de prueba
        productor, created = Productor.objects.get_or_create(
            nif='12345678Z',
            defaults={
                'nombre': 'Juan',
                'apellidos': 'Pérez García',
                'direccion': 'Calle del Olivo 5, Jaén',
                'telefono': '600123456',
                'email': 'juan@ejemplo.com'
            }
        )
        if created:
            self.stdout.write(f'Productor {productor.nombre} creado.')

        # 2. Crear 3 Lotes de Materia Prima
        for i in range(3):
            lote = LoteMateriaPrima.objects.create(
                productor=productor,
                fecha_cosecha=timezone.now().date(),
                peso_bruto=2000.0 + random.uniform(10, 500),
                peso_tara=500.0,
                estado='ANALIZADO' # Los ponemos como analizados para que puedan ir a produccion
            )
            self.stdout.write(f'Lote de materia prima {lote.codigo} creado.')

        # 3. Crear un Lote de Producción de forma segura
        # Generamos un número aleatorio para que el código no se repita
        codigo_nuevo = str(random.randint(1000, 9999))
        
        lote_p = LoteProduccion.objects.create(
            estado='ARMADO',
            codigo_seguimiento=f"POP-{codigo_nuevo}" # Le damos un código único
        )
        
        todos_los_lotes = LoteMateriaPrima.objects.all()
        lote_p.lotes_materia_prima.set(todos_los_lotes)
        lote_p.save()