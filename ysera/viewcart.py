from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Cart, CartItem, Product, ProductImage,OfferImage
from datetime import datetime,timedelta
def cart(request):
    return render(request,"shoppingcart.html")