# Generated by Django 5.1.5 on 2025-02-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0011_alter_shipment_id_alter_shipment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='name',
            field=models.TextField(max_length=14, verbose_name='Nombre de la ruta'),
        ),
    ]
