from django.db import models

#modelo evento
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100, blank=True)

#modelo participante
class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE) #eliminar en cascada


