from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('index/', views.index, name='index'),
    
    path('a-propos/', views.a_propos, name='a-propos'),
    path('commande/', views.commande, name='commande'),
    ]
