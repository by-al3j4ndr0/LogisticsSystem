import uuid
import os

from django.db import models

def rename_file(instance, filename):
    path = "transferencias/"
    format = "transference-%d.xlsx" % instance.id
    return os.path.join(path, format)

class Transference(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.TextField(verbose_name="Nombre", blank=False, null=False, max_length=36, default=uuid.uuid4)
    date = models.DateField(verbose_name="Fecha", editable=False, auto_now_add=True)
    file = models.FileField(verbose_name="Archivo", upload_to=rename_file)

    def __str__(self):
        return self.name