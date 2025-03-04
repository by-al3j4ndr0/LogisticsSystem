# Generated by Django 5.1.5 on 2025-03-02 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0016_alter_transference_name'),
        ('warehouse', '0005_alter_warehouse_hbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='transference_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.transference'),
        ),
        migrations.CreateModel(
            name='WarehouseSimplified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=300, verbose_name='Destinatario')),
                ('ci', models.TextField(max_length=11, verbose_name='Carnet de Identidad')),
                ('phone_number', models.TextField(max_length=30, verbose_name='Numero Telefonico')),
                ('address', models.TextField(max_length=300, verbose_name='Direccion')),
                ('city', models.TextField(max_length=100, verbose_name='Municipio')),
                ('state', models.TextField(max_length=30, verbose_name='Provincia')),
                ('quantity', models.IntegerField(default=1, null=True, verbose_name='Bultos')),
                ('tariff', models.FloatField(verbose_name='Arancel')),
                ('transference_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transfer.transference')),
            ],
        ),
    ]
