from django.db.models import Sum
from .models import Product, Cart
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
@csrf_exempt
@login_required
def add_to_cart(request):
    if request.method == "POST":
        print("test", request.POST)
        product_id = request.POST.get("product_id")
        product = Product.objects.filter(id=product_id).first()
        if product:
            try:
                cart = Cart.objects.get(product_id=product.id, user=request.user.id)
                cart.count = int(cart.count) + 1
                cart.total = cart.total + product.price
                cart.save()
                return JsonResponse(
                    {"success": "This item quantity was updated."}, status=200
                )
            except Cart.DoesNotExist:
                Cart.objects.create(
                    user=request.user, product=product, count=1, total=product.price
                )
                return JsonResponse(
                    {"success": "This item was added to your cart."}, status=200
                )
        else:
            return JsonResponse({"error": "Product not found"}, status=404)
    return render(request, "shop.html")


@login_required
def my_cart(request):
    cart_item = Cart.objects.filter(user_id=request.user.id).select_related('product')
    context = {
        "items": cart_item,
        "total": cart_item.aggregate(total_price=Sum('total')),
        "total_items": cart_item.aggregate(item=Sum('count'))
    }
    return render(request, "products/cart_details.html", context)
