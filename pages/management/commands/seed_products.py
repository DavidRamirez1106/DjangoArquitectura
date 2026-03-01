from django.core.management.base import BaseCommand

try:
    from pages.factories import ProductFactory
    HAS_FACTORY = True
except ImportError:
    HAS_FACTORY = False
    from pages.models import Product


class Command(BaseCommand):
    help = 'Seed the database with products'

    def handle(self, *args, **kwargs):
        if HAS_FACTORY:
            ProductFactory.create_batch(8)
        else:
            # Fallback: create products without factory_boy
            products = [
                {"name": "TV", "price": 299},
                {"name": "iPhone", "price": 999},
                {"name": "Chromecast", "price": 49},
                {"name": "Glasses", "price": 149},
                {"name": "Laptop", "price": 899},
                {"name": "Tablet", "price": 399},
                {"name": "Speaker", "price": 129},
                {"name": "Headphones", "price": 199},
            ]
            for p in products:
                Product.objects.create(name=p["name"], price=p["price"])
        self.stdout.write(self.style.SUCCESS('Successfully seeded products'))
