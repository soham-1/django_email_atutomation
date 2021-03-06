# Generated by Django 4.0 on 2022-01-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(choices=[('MU', 'Mumbai'), ('DL', 'Delhi'), ('CH', 'Chennai'), ('BG', 'Banglore'), ('KO', 'Kolkata')], default='Mumbai', max_length=2)),
                ('send_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
