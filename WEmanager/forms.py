# blog/forms.py
from django import forms
from .models import Abonne, Releve, Facture, Paiement
class ReleveForm(forms.ModelForm):
    class Meta:
        model = Releve
        fields = ['abonne_id', 'mois', 'consommation', 'date_releve']
        widgets = {
            'abonne_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Id de l\'abonne',
        }),
        'mois': forms.Select(attrs={
            'class': 'form-select',
        }),
        'consommation': forms.NumberInput(attrs={
            'class': 'form-input',
            'placeholder': 'Consommation',
            'step': 0.01
        }),
        'date_releve': forms.DateInput(attrs={
            'class': 'form-input',
            'type': 'date'
        })
        },
        
        labels = {
            'abonne_id': 'Id de l\'abonne',
            'mois': 'Mois',
            'consommation': 'Consommation',
            'date_releve': 'Date du relevé',
 }
class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['nom', 'telephone', 'adresse', 'numero_compteur', 'type_adonnement']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nom de l\'abonne',
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Téléphone',
            }),
            'adresse': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Adresse',
            }),
            'numero_compteur': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Numéro de compteur',
            }),
            'type_adonnement': forms.Select(attrs={
                'class': 'form-select',
            })
       
        },
        
        labels = {
            'nom': 'Nom de l\'abonne',
            'telephone': 'Téléphone',
            'adresse': 'Adresse',
            'numero_compteur': 'Numéro de compteur',
            'type_adonnement': 'Type d\'abonnement',
        }
class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['abonne_id', 'releve_id', 'montant', 'date_emission', 'statut']
        widgets = {
            'abonne_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Id de l\'abonne',
            }),
            'releve_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Id du relevé',
            }),
            'montant': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Montant',
                'step': 0.01
            }),
            'date_emission': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
            'statut': forms.Select(attrs={
                'class': 'form-select',
            })
        },
        
        labels = {
            'abonne_id': 'Id de l\'abonne',
            'releve_id': 'Id du relevé',
            'montant': 'Montant',
            'date_emission': 'Date d\'émission',
            'statut': 'Statut de la facture',
        }
class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['facture_id', 'montant', 'date']
        widgets = {
            'facture_id': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Id de la facture',
            }),
            'montant': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Montant',
                'step': 0.01
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            })
        },
        
        labels = {
            'facture_id': 'Id de la facture',
            'montant': 'Montant',
            'date': 'Date du paiement',
        }         
