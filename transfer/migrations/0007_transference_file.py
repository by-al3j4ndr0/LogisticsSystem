# Generated by Django 5.1.5 on 2025-02-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_alter_transference_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transference',
            name='file',
            field=models.FileField(default='settings.MEDIA_ROOT/transfecences/', upload_to='', verbose_name='Archivo'),
        ),
    ]
