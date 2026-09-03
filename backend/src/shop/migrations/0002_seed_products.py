from django.db import migrations


PRODUCTS = [
    ('Wax', 'Wax Soleil d Accra', 9500, 'linen-sage.jpg'),
    ('Wax', 'Wax Indigo du Sahel', 10500, 'silk-floral.jpg'),
    ('Wax', 'Wax Pagne Royal', 12500, 'velvet-sapphire.jpg'),
    ('Wax', 'Wax Feuilles de Baobab', 8900, 'hero-textile.jpg'),
    ('Wax', 'Wax Ankara Émeraude', 11500, 'linen-sage.jpg'),
    ('Bogolan', 'Bogolan Terre de Ségou', 14500, 'silk-floral.jpg'),
    ('Bogolan', 'Bogolan Graphique Noir', 15500, 'velvet-sapphire.jpg'),
    ('Bogolan', 'Bogolan Sable et Carbone', 13800, 'hero-textile.jpg'),
    ('Bogolan', 'Bogolan Rouge Latérite', 14900, 'linen-sage.jpg'),
    ('Bogolan', 'Bogolan Motifs Anciens', 16200, 'silk-floral.jpg'),
    ('Kente', 'Kente Or du Ghana', 19800, 'velvet-sapphire.jpg'),
    ('Kente', 'Kente Vert Forêt', 21500, 'hero-textile.jpg'),
    ('Kente', 'Kente Cobalt et Safran', 22500, 'linen-sage.jpg'),
    ('Kente', 'Kente Fuchsia Royal', 20900, 'silk-floral.jpg'),
    ('Kente', 'Kente Nuit Étoilée', 23500, 'velvet-sapphire.jpg'),
    ('Indigo', 'Indigo de Bamako', 13200, 'hero-textile.jpg'),
    ('Indigo', 'Indigo Nuages du Mali', 14500, 'linen-sage.jpg'),
    ('Indigo', 'Indigo Lignes Nomades', 12800, 'silk-floral.jpg'),
    ('Indigo', 'Indigo Profond Artisanal', 15800, 'velvet-sapphire.jpg'),
    ('Indigo', 'Indigo Pois Contemporains', 13900, 'hero-textile.jpg'),
    ('Faso Dan Fani', 'Faso Dan Fani Ivoire', 17500, 'linen-sage.jpg'),
    ('Faso Dan Fani', 'Faso Dan Fani Terre Rouge', 18900, 'silk-floral.jpg'),
    ('Faso Dan Fani', 'Faso Dan Fani Rayures Fines', 19500, 'velvet-sapphire.jpg'),
    ('Faso Dan Fani', 'Faso Dan Fani Noir et Blanc', 18200, 'hero-textile.jpg'),
    ('Faso Dan Fani', 'Faso Dan Fani Safran', 20500, 'linen-sage.jpg'),
    ('Imprimés', 'Imprimé Ankara Hibiscus', 10800, 'silk-floral.jpg'),
    ('Imprimés', 'Imprimé Ankara Tropical', 11200, 'velvet-sapphire.jpg'),
    ('Imprimés', 'Imprimé Feuillage Lagos', 9900, 'hero-textile.jpg'),
    ('Imprimés', 'Imprimé Géométrique Dakar', 10400, 'linen-sage.jpg'),
    ('Imprimés', 'Imprimé Corail du Littoral', 11800, 'silk-floral.jpg'),
]


def seed_products(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    Product.objects.bulk_create([
        Product(
            category=category,
            name=name,
            price=price,
            image=f'shop/images/{image}',
            is_new=index > 24,
        )
        for index, (category, name, price, image) in enumerate(PRODUCTS, start=1)
    ])


def remove_products(apps, schema_editor):
    apps.get_model('shop', 'Product').objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_products, remove_products),
    ]
