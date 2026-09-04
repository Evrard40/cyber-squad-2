
from django.shortcuts import render


def accueil(request):
    return render(request, 'accueil.html')

def a_propos(request):
    return render(request, 'a propos.html')


def commande(request):
    return render(request, 'commande.html')


def index(request):
    return render(request, 'index.html')


