# Generated by Django 5.1.3 on 2024-11-30 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'db_table': 'cars_brands',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ModelCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model_car', models.CharField(max_length=25)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_models', to='dropout_cars.brandsmodel')),
            ],
            options={
                'db_table': 'cars_models',
                'ordering': ['id'],
            },
        ),
    ]
