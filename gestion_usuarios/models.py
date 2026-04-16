from django.db import models

class Productor(models.Model):
    # Definimos los campos según el enunciado [cite: 9]
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    nif = models.CharField(max_length=9, unique=True, verbose_name="NIF/DNI")
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        # Esto es lo que se verá en el panel de administrador
        return f"{self.nombre} {self.apellidos} ({self.nif})"

    class Meta:
        verbose_name_plural = "Productores"