import os.path

from django.db import models
import uuid

class Clients(models.Model):
    hbl = models.TextField(verbose_name="Codigo de Envio", blank=False, null=False)
    weight = models.FloatField(verbose_name="Peso")
    description = models.TextField(verbose_name="Descripcion")
    name = models.TextField(verbose_name="Nombre y Apellidos")
    ci = models.TextField(verbose_name="Carnet de Identidad")
    phone = models.TextField(verbose_name="Telefono")
    address = models.TextField(verbose_name="Direccion")
    province = models.TextField(verbose_name="Provincia")
    city = models.TextField(verbose_name="Provincia")
    tariff = models.FloatField(verbose_name="Arancel")

    def __str__(self):
        return self.hbl

def rename_file(instance, filename):
    path = "manifiestos/"
    format = "manifest-" + str(instance.id) + ".xlsx"
    return os.path.join(path, format)

class Manifest(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    file = models.FileField(verbose_name="Manifiesto", upload_to=rename_file)