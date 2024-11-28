
# Generated by Django 5.1.3 on 2024-11-28 21:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carsmodel',
            name='bad_words',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='carsmodel',
            name='description',
            field=models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
