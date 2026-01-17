from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Cart, CartItem, Product, ProductImage,OfferImage
from datetime import datetime,timedelta

def cart(request):
    products = []
    price=0
    log='0'
    if not request.user.is_authenticated:
        log='1'
    else:
        cart, created = Cart.objects.get_or_create(user=request.user)
        products = CartItem.objects.filter(cart=cart).count
    c={
        "cart":products,
        "price":price,
        "log":log,
        "is_logged_in": request.user.is_authenticated,
        "user": request.user if request.user.is_authenticated else None,
    }
    return render(request,"shoppingcart.html",c)


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect("login")

    product = get_object_or_404(Product, slug=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    quantity = int(request.POST.get("quantity", 1))

    # Check if product already in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    return redirect("cart")