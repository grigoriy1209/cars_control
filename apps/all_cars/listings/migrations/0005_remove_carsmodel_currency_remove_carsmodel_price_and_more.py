# Generated by Django 5.1.3 on 2024-11-29 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_remove_carsmodel_bad_words_alter_carsmodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carsmodel',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='carsmodel',
            name='price',
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='body_type',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('hatchback', 'Hatchback'), ('suv', 'Suv'), ('crossover', 'Crossover'), ('coupe', 'Coupe'), ('convertible', 'Convertible'), ('wagon', 'Wagon'), ('pickup', 'Pickup'), ('minivan', 'Minivan'), ('van', 'Van'), ('roadster', 'Roadster'), ('luxury_car', 'Luxury Car'), ('sport_car', 'Sport Car')], max_length=25),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
