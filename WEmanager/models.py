from django.db import models
from django.db import models 
from django.utils import timezone

class Abonne(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    telephone  = models.IntegerField(unique=True)
    adresse = models.CharField(max_length=200)
    numero_compteur = models.CharField(max_length=20)
    type_adonnement = models.CharField(max_length=100)

class Releve(models.Model):
    abonne_id = models.ForeignKey(Abonne, on_delete = models.CASCADE ,unique=True)
    mois = models.CharField(max_length=10)
    consommation = models.FloatField(max_length=20)
    date_releve = models.DateField(default=timezone.now)

class Facture(models.Model):
    abonne_id = models.ForeignKey(Abonne, on_delete = models.CASCADE, unique=True)
    releve_id = models.ForeignKey(Releve, on_delete = models.CASCADE ,unique=True)
    montant = models.FloatField(max_length=20)
    date_emission = models.DateField(default=timezone.now)
    statut = models.CharField(max_length=50)

class Paiement(models.Model):
    facture_id = models.ForeignKey(Facture, on_delete=models.CASCADE)
    montant = models.FloatField(max_length=20)
    date = models.DateField(default=timezone.now)
# Create your models here.
