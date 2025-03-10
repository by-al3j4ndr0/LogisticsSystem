# Generated by Django 5.1.5 on 2025-02-09 14:58

import transfer.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0012_alter_transference_date_alter_transference_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transference',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='transference',
            name='file',
            field=models.FileField(upload_to=transfer.models.rename_file, verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='transference',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transference',
            name='name',
            field=models.TextField(default=uuid.uuid4, max_length=36, verbose_name='Nombre'),
        ),
    ]
