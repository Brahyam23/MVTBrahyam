# Generated by Django 4.0.6 on 2022-07-27 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familiar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='anio_nac',
        ),
    ]
