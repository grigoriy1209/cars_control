# Generated by Django 5.1.3 on 2024-11-25 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_remove_carsmodel_is_active_carsmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsmodel',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='description',
            field=models.TextField(blank=True, max_length=500, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='active', max_length=20),
        ),
    ]