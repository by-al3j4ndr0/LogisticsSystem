# Generated by Django 5.1.5 on 2025-02-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_clients_status'),
        ('shipment', '0009_alter_shipment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='clients',
        ),
        migrations.AddField(
            model_name='shipment',
            name='clients',
            field=models.ManyToManyField(to='clients.clients', verbose_name='Clientes'),
        ),
    ]
