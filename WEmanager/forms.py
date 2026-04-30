from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Abonne, Releve, Facture, Paiement
class ReleveForm(forms.ModelForm):
    class Meta:
        model = Releve
        fields = ['abonne', 'mois', 'consommation', 'date_releve']
        widgets = {
            'abonne': forms.Select(attrs={'class': 'form-select'}),
            'mois': forms.Select(attrs={'class': 'form-select'}),
            'consommation': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Consommation',
                'step': 0.01
            }),
            'date_releve': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
        }
class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['nom', 'telephone', 'adresse', 'numero_compteur', 'type_abonne']
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
            'type_abonne': forms.Select(attrs={
                'choices': [('eau', 'Eau'), ('electricite', 'Électricité')],
                'class': 'form-select',
            })
       
        },
        
        labels = {
            'nom': 'Nom de l\'abonne',
            'telephone': 'Téléphone',
            'adresse': 'Adresse',
            'numero_compteur': 'Numéro de compteur',
            'type_abonne': 'Type d\'abonnement',
        }
class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['abonne', 'releve', 'montant', 'date_emission', 'statut']
        widgets = {
            'abonne': forms.Select(attrs={'class': 'form-select'}),
            'releve': forms.Select(attrs={'class': 'form-select'}),
            'montant': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Montant',
                'step': 0.01
            }),
            'date_emission': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }
class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['facture', 'montant', 'date']
        widgets = {
            'facture': forms.Select(attrs={'class': 'form-select'}),
            'montant': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Montant',
                'step': 0.01
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            })
        }
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nom d\'utilisateur',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email',
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Mot de passe',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'Confirmer le mot de passe',
            }),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Nom d\'utilisateur',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-input',
        'placeholder': 'Mot de passe',
    }))         
