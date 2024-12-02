# Generated by Django 5.1.3 on 2024-12-01 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0002_alter_autosaloonmodel_address_and_more'),
        ('listings', '0003_rename_autosaloon_carsmodel_auto_saloon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsmodel',
            name='auto_saloon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='dealerships.autosaloonmodel'),
        ),
    ]