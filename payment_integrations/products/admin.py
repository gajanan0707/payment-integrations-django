from django.contrib import admin
from .models import Product, Cart


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "brand", "price", "rating")
    search_fields = ("name", "brand", "category")


class CartAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "count", "total")
    search_fields = ("product", "user")


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
