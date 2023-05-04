import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from apps.cart.cart import Cart

from .models import Product

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



