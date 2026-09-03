from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('collection/', views.collection, name='collection'),
    path('collection', views.collection),
    path('nouveautes/', views.nouveautes, name='nouveautes'),
    path('nouveautes', views.nouveautes),
    path('api/produits/', views.liste_produits, name='liste-produits'),
    path('api/commandes/', views.creer_commande, name='creer-commande'),
]
