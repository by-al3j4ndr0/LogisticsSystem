# Generated by Django 5.1.5 on 2025-02-08 20:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0005_transference_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transference',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
    ]
