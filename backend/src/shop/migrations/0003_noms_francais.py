from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('shop', '0002_seed_products')]

    operations = [
        migrations.RenameModel('Product', 'Produit'),
        migrations.RenameModel('Order', 'Commande'),
        migrations.RenameModel('OrderItem', 'ArticleCommande'),
        migrations.RenameField('Produit', 'category', 'categorie'),
        migrations.RenameField('Produit', 'name', 'nom'),
        migrations.RenameField('Produit', 'price', 'prix'),
        migrations.RenameField('Produit', 'is_new', 'est_nouveau'),
        migrations.RenameField('Produit', 'is_active', 'est_actif'),
        migrations.RenameField('Produit', 'created_at', 'cree_le'),
        migrations.RenameField('Commande', 'customer_name', 'nom_client'),
        migrations.RenameField('Commande', 'customer_email', 'email_client'),
        migrations.RenameField('Commande', 'status', 'statut'),
        migrations.RenameField('Commande', 'created_at', 'cree_le'),
        migrations.RenameField('ArticleCommande', 'order', 'commande'),
        migrations.RenameField('ArticleCommande', 'product', 'produit'),
        migrations.RenameField('ArticleCommande', 'meters', 'metres'),
        migrations.RenameField('ArticleCommande', 'unit_price', 'prix_unitaire'),
    ]