# Generated by Django 5.1.5 on 2025-02-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_delete_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transference',
            name='name',
            field=models.TextField(max_length=30, null=True, verbose_name='Nombre'),
        ),
    ]
