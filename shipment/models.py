from django.db import models
from clients.models import Clients

class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    name = models.TextField(verbose_name="Nombre de la ruta", max_length=13)
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Fecha", editable=False, auto_now_add=True)

    def __str__(self):
        return self.name
