# Generated by Django 5.1.3 on 2024-12-01 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dealerships', '0002_alter_autosaloonmodel_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autosaloonmodel',
            old_name='owner',
            new_name='user',
        ),
    ]
