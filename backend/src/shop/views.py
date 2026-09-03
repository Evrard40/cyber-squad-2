import json
from decimal import Decimal, InvalidOperation

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from .models import ArticleCommande, Commande, Produit


def donnees_produit(produit, prefixe_champ='metre'):
    return {
        'id': produit.id,
        'categorie': produit.categorie,
        'nom': produit.nom,
        'prix': produit.prix,
        'image': produit.image,
        'identifiant_champ': f'{prefixe_champ}-{produit.id}',
    }


def accueil(request):
    return render(request, 'index.html')


def collection(request):
    produits_actifs = Produit.objects.filter(est_actif=True)
    produits = [donnees_produit(produit) for produit in produits_actifs]
    categories = ['Toutes'] + list(
        produits_actifs.values_list('categorie', flat=True).distinct().order_by('categorie')
    )
    return render(request, 'collection.html', {'produits': produits, 'categories': categories})


def nouveautes(request):
    produits = [
        donnees_produit(produit, 'nouveau-metre')
        for produit in Produit.objects.filter(est_actif=True, est_nouveau=True)
    ]
    return render(request, 'nouveaute.html', {'produits': produits})


@require_GET
def liste_produits(request):
    produits = [donnees_produit(produit) for produit in Produit.objects.filter(est_actif=True)]
    return JsonResponse({'produits': produits, 'nombre': len(produits)})


@require_POST
def creer_commande(request):
    try:
        payload = json.loads(request.body)
        client = payload.get('client', {})
        articles = payload.get('articles', [])
        nom = str(client.get('nom', '')).strip()
        email = str(client.get('email', '')).strip()
        if not nom or not email or not articles:
            return JsonResponse({'error': 'Nom, email et articles sont obligatoires.'}, status=400)

        with transaction.atomic():
            articles_valides = []
            total = 0
            for article in articles:
                produit = Produit.objects.get(pk=article.get('produit_id'), est_actif=True)
                metres = Decimal(str(article.get('metres', '0')))
                if metres <= 0 or metres % Decimal('0.5') != 0:
                    return JsonResponse({'error': 'La longueur doit etre un multiple de 0,5 metre.'}, status=400)
                articles_valides.append((produit, metres))
                total += int(metres * produit.prix)

            commande = Commande.objects.create(nom_client=nom, email_client=email, total=total)
            for produit, metres in articles_valides:
                ArticleCommande.objects.create(
                    commande=commande,
                    produit=produit,
                    metres=metres,
                    prix_unitaire=produit.prix,
                )
    except (json.JSONDecodeError, TypeError, ValueError, InvalidOperation):
        return JsonResponse({'error': 'Format de commande invalide.'}, status=400)
    except Produit.DoesNotExist:
        return JsonResponse({'error': 'Un produit est introuvable ou indisponible.'}, status=400)

    return JsonResponse({'id': commande.id, 'statut': commande.statut, 'total': commande.total}, status=201)
