import json

from django.test import TestCase

from .models import Commande, Produit


class TestsBoutique(TestCase):
	fixtures = []

	def setUp(self):
		self.produit = Produit.objects.create(
			categorie='Wax',
			nom='Wax Test',
			prix=10000,
			image='shop/images/test.jpg',
		)

	def test_api_produits_retourne_produits_actifs(self):
		response = self.client.get('/api/produits/')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.json()['nombre'], Produit.objects.filter(est_actif=True).count())
		produit = next(item for item in response.json()['produits'] if item['nom'] == 'Wax Test')
		self.assertEqual(produit['prix'], 10000)

	def test_api_commande_recalcule_total_cote_serveur(self):
		response = self.client.post(
			'/api/commandes/',
			data=json.dumps({
				'client': {'nom': 'Awa', 'email': 'awa@example.com'},
				'articles': [{'produit_id': self.produit.id, 'metres': 1.5}],
			}),
			content_type='application/json',
		)

		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.json()['total'], 15000)
		self.assertEqual(Commande.objects.count(), 1)

	def test_api_commande_refuse_longueur_invalide(self):
		response = self.client.post(
			'/api/commandes/',
			data=json.dumps({
				'client': {'nom': 'Awa', 'email': 'awa@example.com'},
				'articles': [{'produit_id': self.produit.id, 'metres': 1.2}],
			}),
			content_type='application/json',
		)

		self.assertEqual(response.status_code, 400)
		self.assertEqual(Commande.objects.count(), 0)
