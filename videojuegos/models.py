from django.db import models

class Videojuego(models.Model):
    # Django creará automáticamente un campo id_videojuego (pk)
    nombre = models.CharField(max_length=100)
    # max_digits: total de dígitos (5), decimal_places: decimales (2)
    duracion_horas = models.DecimalField(max_digits=5, decimal_places=2) 
    ao_lanzamiento = models.IntegerField()

    class Meta:
        # Esto asegura que Django use una tabla llamada 'videojuegos'
        db_table = 'videojuegos' 

    def __str__(self):
        return f'{self.nombre} ({self.ao_lanzamiento})'