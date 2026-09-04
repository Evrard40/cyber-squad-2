from django.contrib import admin

from .models import  Commande, Produit , Profil, Achat,Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
	list_display = ['nom']

@admin.register(Produit)
class AdministrationProduit(admin.ModelAdmin):
	list_display = ('nom', 'categorie', 'prix', 'est_nouveau', 'est_disponible','image','stock')
	list_filter = ('categorie', 'est_nouveau', 'est_disponible')
	search_fields = ('nom', 'categorie')


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
	list_display = ['numero_telephone','utilisateur']

@admin.register(Achat)
class AchatAdmin(admin.ModelAdmin):
	list_display = ['produit','utilisateur','quantite','montant','date_achat']

@admin.register(Commande)
class AdministrationCommande(admin.ModelAdmin):
	list_display = ('utilisateur',  'cree_le','type_de_commande','recu_par_client')
	list_filter = ('recu_par_client', 'cree_le')


