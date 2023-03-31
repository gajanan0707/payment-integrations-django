from django.urls import path
from .views import home, about, contact_us, shop

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("shop/", shop, name="shop"),
    path("contact_us/", contact_us, name="contact_us"),
]
