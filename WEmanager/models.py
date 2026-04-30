from django.utils import timezone
from django.db import models

class Abonne(models.Model):
    nom = models.CharField(max_length=100 )
    telephone = models.CharField(max_length=20, unique=True)
    adresse = models.CharField(max_length=200)
    numero_compteur = models.CharField(max_length=20, unique=True)
    type_abonne = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} : ({self.numero_compteur})"


class Releve(models.Model):
    abonne = models.ForeignKey(Abonne, on_delete=models.CASCADE)
    mois = models.CharField(max_length=10)
    consommation = models.FloatField()
    date_releve = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.abonne.nom} - {self.mois} : {self.consommation}"


class Facture(models.Model):
    abonne = models.ForeignKey(Abonne, on_delete=models.CASCADE)
    releve = models.ForeignKey(Releve, on_delete=models.CASCADE)
    montant = models.FloatField()
    date_emission = models.DateField(default=timezone.now)
    statut = models.CharField(max_length=50, default='Non payé')

    def __str__(self):
        return f"Facture {self.abonne.nom} - {self.montant}"


class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    montant = models.FloatField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Paiement {self.montant}"