from django.shortcuts import render
from .cart import Cart
def CartDetail(request):
    cart = Cart(request)


    context = {
        'cart':cart
    }
    return render(request,'cart.html', context)
