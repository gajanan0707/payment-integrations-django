from django import template
from products.models import Cart

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Cart.objects.filter(user=user).count()
        return qs
    return 0
