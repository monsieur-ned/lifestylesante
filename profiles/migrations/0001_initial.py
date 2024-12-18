# Generated by Django 5.1.4 on 2024-12-11 01:45

import django.db.models.deletion
import django_countries.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('sexe', models.CharField(choices=[('F', 'Féminin'), ('M', 'Masculin')], max_length=1, verbose_name='Sexe')),
                ('date_naissance', models.DateField(blank=True, null=True, verbose_name='Date de naissance')),
                ('lieu_naissance', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lieu de naissance')),
                ('nationalite', django_countries.fields.CountryField(max_length=2, verbose_name='Nationalité')),
                ('adresse', models.TextField(verbose_name='Adresse')),
                ('telephone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('fonction', models.CharField(max_length=100, null=True, verbose_name='Fonction')),
                ('departement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Département')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='employe_photos/', verbose_name='Photo')),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/', verbose_name='QR Code')),
                ('auth_token', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="Token d'authentification")),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Info bio')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Date et heure de création')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='MarquerArrivee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivee', models.BooleanField(default=True)),
                ('date_arrivee', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.employe')),
            ],
        ),
        migrations.CreateModel(
            name='MarquerDepart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.BooleanField(default=True)),
                ('date_depart', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('date_arrivee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.marquerarrivee')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.employe')),
            ],
        ),
    ]
