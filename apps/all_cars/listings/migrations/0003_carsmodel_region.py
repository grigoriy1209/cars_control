# Generated by Django 5.1.2 on 2024-11-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_carsmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsmodel',
            name='region',
            field=models.CharField(default=1, max_length=23),
            preserve_default=False,
        ),
    ]