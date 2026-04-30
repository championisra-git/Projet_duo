from django.shortcuts import render
from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ReleveForm, AbonneForm, FactureForm, PaiementForm, LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from .models import Abonne, Releve, Facture, Paiement

def home(request):
    return render(request, 'home.html')
@login_required
def liste_abonnes(request):
    search = request.GET.get('search')

    if search:
        abonnes = Abonne.objects.filter(nom__icontains=search)
    else:
        abonnes = Abonne.objects.all()

    return render(request, 'abonnes.html', {'abonnes': abonnes})

# CREATE : Ajouter un abonné
@login_required
def ajouter_abonne(request):
    if request.method == 'POST':
        Abonne.objects.create(
            nom=request.POST.get('nom'),
            telephone=request.POST.get('telephone'),
            numero_compteur=request.POST.get('numero_compteur'),
            type_abonne=request.POST.get('type_abonnement')
        )
        return redirect('abonnes')
    return render(request, 'ajouter_abonne.html')

# UPDATE : Modifier un abonné
@login_required
def modifier_abonne(request, pk):
    abonne = get_object_or_404(Abonne, pk=pk)
    if request.method == 'POST':
        abonne.nom = request.POST.get('nom')
        abonne.telephone = request.POST.get('telephone')
        abonne.numero_compteur = request.POST.get('numero_compteur')
        abonne.type_abonnement = request.POST.get('type_abonnement')
        abonne.save()
        return redirect('abonnes')
    return render(request, 'modifier_abonne.html', {'abonne': abonne})

# DELETE : Supprimer un abonné
@login_required
def supprimer_abonne(request, pk):
    abonne = get_object_or_404(Abonne, pk=pk)
    abonne.delete()
    return redirect('abonnes')



# --- CRUD RELEVES ---
@login_required
def liste_releves(request):
    releves = Releve.objects.all().select_related('abonne').order_by('-date_releve')
    return render(request, 'releves.html', {'releves': releves})


@login_required
def ajouter_releve(request):
    if request.method == 'POST':
        form = ReleveForm(request.POST)

        if form.is_valid():
            # 1. créer le relevé sans sauvegarder immédiatement
            releve = form.save(commit=False)

            # 2. récupérer les données
            abonne = releve.abonne
            conso = releve.consommation

            # 3. sauvegarder le relevé
            releve.save()

            # 4. créer la facture liée
            Facture.objects.create(
                abonne=abonne,
                releve=releve,  
                montant=conso * 100,
                statut="En attente"
            )

            messages.success(request, "Relevé créés avec succès.")

            return redirect('modifier_facture_abonne', releve=releve.id)

    else:
        form = ReleveForm()

    return render(request, 'ajouter_releve.html', {'form': form})
@login_required
def modifier_releve(request, pk):
    releve = get_object_or_404(Releve, pk=pk)
    if request.method == 'POST':
        releve.abonne = request.POST.get('abonne')
        releve.mois = request.POST.get('mois')
        releve.consommation = request.POST.get('consommation')
        releve.date_releve = request.POST.get('date_releve')
        releve.save()
        return redirect('factures')
    return render(request, 'modifier_releve.html', {'releve': releve})

# DELETE : Supprimer une facture
@login_required
def supprimer_releve(request, pk):
    releve = get_object_or_404(Releve, pk=pk)
    releve.delete()
    return redirect('releves')
# --- CRUD FACTURES ---
@login_required
def factures(request):
    # On récupère toutes les factures enregistrées
    toutes_les_factures = Facture.objects.all().select_related('abonne')
    
    # On les envoie au template via le dictionnaire (le "context")
    return render(request, 'factures.html', {'factures': toutes_les_factures})

@login_required
def liste_factures(request):
    factures = Facture.objects.all().order_by('-date_emission')
    return render(request, 'factures.html', {'factures': factures})

# UPDATE : Modifier le statut ou le montant
@login_required
def modifier_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.montant = request.POST.get('montant')
        facture.statut = request.POST.get('statut')
        facture.save()
        return redirect('factures')
    return render(request, 'modifier_facture.html', {'facture': facture})

@login_required
def modifier_facture_abonne(request, releve):
    facture = get_object_or_404(Facture, releve=releve)
    if request.method == 'POST':
        facture.statut = request.POST.get('statut')
        facture.save()
        return redirect('factures')
    return render(request, 'modifier_facture.html', {'facture': facture})

# DELETE : Supprimer une facture
@login_required
def supprimer_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    facture.delete()
    return redirect('factures')
@login_required
def ajouter_facture(request, abonne_id=None):
    if request.method == 'POST':
        form =FactureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facture ajoutée avec succès.')
        return redirect('factures')
    else:
        form = FactureForm()
    return render(request, 'ajouter_facture.html', {'form': form})
@login_required
def paiement(request):
    if request.method == 'POST':
        form = PaiementForm(request.POST)
        if form.is_valid():
            state=form.instance.facture.statut
            if state == "En attente":
                paiement = form.save()
                facture = paiement.facture
                facture.statut = "Payée"
                facture.save()
            form.save()
            messages.success(request, 'Paiement effectué avec succès.')
        return redirect('factures')
    else:
        form = PaiementForm()
    return render(request, 'paiement.html', {'form': form})

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
    return render(request, 'logout.html')

def signup(request):
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
    return render(request, 'signup.html')