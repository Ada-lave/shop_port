import datetime
import os

from random import randint
from apps.cart.cart import Cart
from apps.order.models import OrederItem, Order

def checkout(request, first, last, email, address, zipcode, place):
    order = Order(first_name=first, last_name=last, email=email, address=address, zipcode=zipcode, place=place)
    order.save()

    cart = Cart(request)

    for item in cart:
        OrederItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    
    return order.id
