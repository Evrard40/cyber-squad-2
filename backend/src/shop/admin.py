from django.contrib import admin

from .models import ArticleCommande, Commande, Produit


@admin.register(Produit)
class AdministrationProduit(admin.ModelAdmin):
	list_display = ('nom', 'categorie', 'prix', 'est_nouveau', 'est_actif')
	list_filter = ('categorie', 'est_nouveau', 'est_actif')
	search_fields = ('nom', 'categorie')


class ArticleCommandeEnLigne(admin.TabularInline):
	model = ArticleCommande
	extra = 0
	readonly_fields = ('prix_unitaire',)


@admin.register(Commande)
class AdministrationCommande(admin.ModelAdmin):
	list_display = ('id', 'nom_client', 'email_client', 'total', 'statut', 'cree_le')
	list_filter = ('statut', 'cree_le')
	search_fields = ('nom_client', 'email_client')
	inlines = [ArticleCommandeEnLigne]
