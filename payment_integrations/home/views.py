from products.models import Product, Cart
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def shop(request):
    products = Product.objects.all().values("id", "name", "price", "image", "rating")
    return render(request, "shop.html", context={"products": products})


def contact_us(request):
    return render(request, "contact.html")
