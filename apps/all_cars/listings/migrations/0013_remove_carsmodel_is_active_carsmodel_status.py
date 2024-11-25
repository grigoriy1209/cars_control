# Generated by Django 5.1.3 on 2024-11-25 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_remove_carsmodel_status_carsmodel_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carsmodel',
            name='is_active',
        ),
        migrations.AddField(
            model_name='carsmodel',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]