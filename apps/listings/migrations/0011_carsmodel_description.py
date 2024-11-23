# Generated by Django 5.1.3 on 2024-11-22 22:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_remove_carsmodel_edit_count_alter_carsmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsmodel',
            name='description',
            field=models.TextField(default=1, max_length=500, validators=[django.core.validators.MinLengthValidator(2)]),
            preserve_default=False,
        ),
    ]
