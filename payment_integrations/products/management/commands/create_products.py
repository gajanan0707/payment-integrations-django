import requests
from products.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get("https://dummyjson.com/products")
        for product in response.json().get("products"):
            if not Product.objects.filter(name__iexact=product.get("title")).exists():
                data = {
                    "name": product.get("title"),
                    "price": product.get("price"),
                    "description": product.get("description"),
                    "thumbnail": product.get("thumbnail"),
                    "image": product.get("images")[0],
                    "rating": product.get("rating"),
                    "brand": product.get("brand"),
                    "category": product.get("category"),
                }
                Product.objects.create(**data)
