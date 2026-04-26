from django.shortcuts import render
from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReleveForm, AbonneForm, FactureForm, PaiementForm
from .models import Abonne, Releve, Facture, Paiement

def login_view(request):
    return render(request, 'login.html' )

def logout_view(request):
    return render(request, 'logout.html')

def signup_view(request):
    return render(request, 'signup.html')

@login_required
def enregistrement_relevé(request):

    return render(request, 'enregistrement_relevé.html' )

@login_required
def enregistrement_abonne(request):

    return render(request, 'abonne.html' )

@login_required
def enregistrement_facture(request):

    return render(request, 'facture.html' )

@login_required
def enregistrement_paiement(request):

    return render(request, 'paiement.html' )





def home(request):

    return render(request, 'home.html' )


# Create your views here.
