from django.urls import path

from .views import add_to_cart, my_cart

urlpatterns = [
    path("add-to-cart", add_to_cart, name="add_to_cart"),
    path("my-cart", my_cart, name="my-cart"),
]
