# Generated by Django 4.2.16 on 2024-10-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connexion',
            name='photo',
            field=models.ImageField(upload_to='connexion'),
        ),
    ]
