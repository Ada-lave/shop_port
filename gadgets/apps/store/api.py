import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from apps.cart.cart import Cart
from apps.order.utils import checkout

from .models import Product
from apps.order.models import Order, OrederItem
from apps.cart.cart import Cart

def ApiCheckout(request):
    data = json.loads(request.body)
    jsonresp = {'success':True}
    cart = Cart(request)

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    address = data['address']
    zipcode = data['zipcode']
    place = data['place']

    order_id = checkout(request, first_name, last_name, email, address, zipcode, place)

    paid = True

    if paid==True:
        order = Order.objects.get(pk=order_id)
        order.paid = True
        order.paidAmount = cart.TotalPrice()
        order.save()

        cart.clear()
    return JsonResponse(jsonresp)

def ApiAddToCart(request):
    data = json.loads(request.body)
    jsonresponce = {'success':True}
    product_id = data['product_id']
    update = data['update']
    quantity = data['quantity']

    


    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    if not update:
        cart.add(product=product, quantity=1, update_q=False)
    elif update=='inc':
        cart.add(product=product, quantity=quantity, update_q='inc')
    else:
        cart.add(product=product, quantity=quantity, update_q=True)

    
    return JsonResponse(jsonresponce)

def ApiRemoveCart(request):
    data = json.loads(request.body)
    jsonresponce = {'success':True}
    product_id = str(data['product_id'])

    cart = Cart(request)
    cart.remove(product_id=product_id)

    return JsonResponse(jsonresponce)



