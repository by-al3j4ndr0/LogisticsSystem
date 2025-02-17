from django.db import models
from clients.models import Clients

class Driver(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    name = models.TextField(verbose_name="Nombre del chofer", max_length=100)
    license = models.TextField(verbose_name="Numero de licencia", max_length=11)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    model = models.TextField(verbose_name="Modelo del vehiculo", max_length=30)
    matriculate = models.TextField(verbose_name="Matricula", max_length=7)

    def __str__(self):
        return self.matriculate

class Shipment(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True)
    name = models.TextField(verbose_name="Nombre de la ruta", max_length=13)
    driver = models.ForeignKey(Driver, verbose_name="Chofer", on_delete=models.CASCADE, null=True)
    vehicle = models.ForeignKey(Vehicle, verbose_name="Vehiculo", on_delete=models.CASCADE, null=True)
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Fecha", editable=False, auto_now_add=True)

    def __str__(self):
        return self.name
