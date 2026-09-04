from django.db import models
from django.contrib.auth.models import User 

class Categorie(models.Model):
	nom = models.CharField(max_length=80)

class Produit(models.Model):

	categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
	nom = models.CharField(max_length=160)
	prix = models.PositiveIntegerField(help_text='Prix en FCFA par metre')
	image = models.ImageField(upload_to='Image/')
	stock = models.PositiveIntegerField(default=0)
	est_nouveau = models.BooleanField(default=False)
	est_disponible = models.BooleanField(default=True)

	def __str__(self):
		return self.nom


	
class Profil(models.Model):
	numero_telephone = models.CharField(max_length=13)
	utilisateur = models.ForeignKey(User,
									  on_delete=models.CASCADE,
		)
	def __str__(self):
		return self.utilisateur

class Achat(models.Model):
	produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
	utilisateur = models.ForeignKey(User,on_delete=models.CASCADE)
	quantite = models.PositiveIntegerField()
	montant = models.DecimalField(max_digits=10,decimal_places=3)
	date_achat = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.produit


class Commande(models.Model):
	CHOIX = (
		('livraison','Livraison'),
		('presentiel','Presentiel')
	)

	utilisateur = models.ForeignKey(User,
								  on_delete=models.CASCADE,
    )
	achat = models.ManyToManyField(Achat)

	type_de_commande = models.CharField(max_length=12,choices=CHOIX)

	recu_par_client = models.BooleanField(default=False)

	cree_le = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.type_de_commande)