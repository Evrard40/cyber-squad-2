from django.db import models


class Produit(models.Model):
	categorie = models.CharField(max_length=80, db_index=True)
	nom = models.CharField(max_length=160)
	prix = models.PositiveIntegerField(help_text='Prix en FCFA par metre')
	image = models.CharField(max_length=255)
	est_nouveau = models.BooleanField(default=False)
	est_actif = models.BooleanField(default=True)
	cree_le = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['categorie', 'nom']

	def __str__(self):
		return self.nom


class Commande(models.Model):
	CHOIX_STATUT = [
		('pending', 'En attente'),
		('confirmed', 'Confirmee'),
		('shipped', 'Expediee'),
		('cancelled', 'Annulee'),
	]

	nom_client = models.CharField(max_length=120)
	email_client = models.EmailField()
	statut = models.CharField(max_length=20, choices=CHOIX_STATUT, default='pending')
	total = models.PositiveIntegerField(default=0)
	cree_le = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-cree_le']

	def __str__(self):
		return f'Commande #{self.pk}'


class ArticleCommande(models.Model):
	commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='articles')
	produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
	metres = models.DecimalField(max_digits=6, decimal_places=1)
	prix_unitaire = models.PositiveIntegerField()

	@property
	def sous_total(self):
		return int(self.metres * self.prix_unitaire)
