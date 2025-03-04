from django.db import models
from transfer.models import Transference

class Warehouse(models.Model):
    hbl = models.TextField(verbose_name="HBL", blank=False, null=False, max_length=13)
    name = models.TextField(verbose_name="Destinatario", blank=False, null=False, max_length=300)
    ci = models.TextField(verbose_name="Carnet de Identidad", blank=False, null=False, max_length=11)
    phone_number = models.TextField(verbose_name="Numero Telefonico", blank=False, null=False, max_length=30)
    address = models.TextField(verbose_name="Direccion", blank=False, null=False, max_length=300)
    city = models.TextField(verbose_name="Municipio", blank=False, null=False, max_length=100)
    state = models.TextField(verbose_name="Provincia", blank=False, null=False, max_length=30)
    tariff = models.FloatField(verbose_name="Arancel", null=False)
    transference_id = models.TextField(verbose_name="ID Transferencia", null=True)

    def __str__(self):
        return self.name

class WarehouseSimplified(models.Model):
    name = models.TextField(verbose_name="Destinatario", blank=False, null=False, max_length=300)
    ci = models.TextField(verbose_name="Carnet de Identidad", blank=False, null=False, max_length=11)
    phone_number = models.TextField(verbose_name="Numero Telefonico", blank=False, null=False, max_length=30)
    address = models.TextField(verbose_name="Direccion", blank=False, null=False, max_length=300)
    city = models.TextField(verbose_name="Municipio", blank=False, null=False, max_length=100)
    state = models.TextField(verbose_name="Provincia", blank=False, null=False, max_length=30)
    quantity = models.IntegerField(verbose_name="Bultos", blank=False, null=True, default=1)
    tariff = models.FloatField(verbose_name="Arancel", null=False)
    transference_id = models.TextField(verbose_name="ID Transferencia", null=True)

    def __str__(self):
        return self.name
