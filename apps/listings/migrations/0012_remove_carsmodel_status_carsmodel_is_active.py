# Generated by Django 5.1.3 on 2024-11-23 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_carsmodel_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carsmodel',
            name='status',
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]