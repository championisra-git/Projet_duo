from django.shortcuts import render
from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import ReleveForm, AbonneForm, FactureForm, PaiementForm, SignupForm, LoginForm
from .models import Abonne, Releve, Facture, Paiement

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Connexion réussie.')
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Déconnexion réussie.')
    return redirect('home')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Inscription réussie.')
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def enregistrement_relevé(request):
    if request.method == "POST":
        form = ReleveForm(request.POST)
        if form.is_valid():
            releve = form.save(commit=False)
            releve.auteur = request.user
            releve.save()
            messages.success(request, 'Relevé enregistré avec succés!')
            return redirect('home')
        else:
            form = ReleveForm()
        return render(request, 'releves.html', {'form': form})

@login_required
def enregistrement_abonne(request):
    if request.method == "POST":
        form = AbonneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Abonné enregistré avec succés!')
            return redirect('home')
    else:
        form = AbonneForm()
    return render(request, 'abonnes.html', {'form': form})

@login_required
def enregistrement_facture(request):

    return render(request, 'facture.html' )

@login_required
def enregistrement_paiement(request):

    return render(request, 'paiement.html' )





def home(request):

    return render(request, 'home.html' )


# Create your views here.
