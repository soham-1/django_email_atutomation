# Generated by Django 4.0 on 2022-01-03 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0002_alter_emailmodels_city'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailModels',
            new_name='EmailModel',
        ),
    ]
