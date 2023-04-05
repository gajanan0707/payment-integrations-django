from django.urls import path
from products.views import add_to_cart

urlpatterns = [
    path("add-to-cart", add_to_cart, name="add_to_cart"),
]
