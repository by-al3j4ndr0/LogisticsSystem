# Generated by Django 5.1.5 on 2025-02-18 15:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0004_alter_shipment_driver_alter_shipment_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
