from django.shortcuts import render, redirect, get_object_or_404
from .models import Abonne,Releve, Facture

def home(request):
    return render(request, 'home.html')

def liste_abonnes(request):
    tous_les_abonnes = Abonne.objects.all()
    return render(request, 'abonnes.html', {'abonnes': tous_les_abonnes})

# CREATE : Ajouter un abonné
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
def supprimer_abonne(request, pk):
    abonne = get_object_or_404(Abonne, pk=pk)
    abonne.delete()
    return redirect('abonnes')



# --- CRUD RELEVES ---
def liste_releves(request):
    releves = Releve.objects.all().select_related('abonne_id')
    return render(request, 'releves.html', {'releves': releves})

def ajouter_releve(request):
    if request.method == 'POST':
        # 1. Récupérer l'abonné et la conso
        abonne = get_object_or_404(Abonne, id=request.POST.get('abonne_id'))
        conso = int(request.POST.get('consommation'))
        
        # 2. Créer le relevé
        Releve.objects.create(
            abonne_id=abonne,
            mois=request.POST.get('mois'),
            consommation=conso
        )
        
        # 3. CRÉER LA FACTURE ICI (Calcul automatique)
        # On multiplie la conso par un prix unitaire (ex: 100)
        Facture.objects.create(
            abonne_id=abonne,
            montant=conso * 100, 
            statut="En attente"
        )
        
        return redirect('factures') # Redirige pour voir la facture générée
    
    return render(request, 'ajouter_releve.html', {'abonnes': Abonne.objects.all()})

# --- CRUD FACTURES ---
def factures(request):
    # On récupère toutes les factures enregistrées
    toutes_les_factures = Facture.objects.all().select_related('abonne_id')
    
    # On les envoie au template via le dictionnaire (le "context")
    return render(request, 'factures.html', {'factures': toutes_les_factures})

def liste_factures(request):
    factures = Facture.objects.all().order_by('-date_emission')
    return render(request, 'factures.html', {'factures': factures})

# UPDATE : Modifier le statut ou le montant
def modifier_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.montant = request.POST.get('montant')
        facture.statut = request.POST.get('statut')
        facture.save()
        return redirect('factures')
    return render(request, 'modifier_facture.html', {'facture': facture})

# DELETE : Supprimer une facture
def supprimer_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    facture.delete()
    return redirect('factures')
def ajouter_facture(request):
    if request.method == 'POST':
        abonne = get_object_or_404(Abonne, id=request.POST.get('abonne_id'))
        Facture.objects.create(
            abonne_id=abonne,
            montant=request.POST.get('montant'),
            statut="En attente"
        )
        return redirect('factures')
    return render(request, 'ajouter_facture.html', {'abonnes': Abonne.objects.all()})

def paiement(request):
    return render(request, 'paiement.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
