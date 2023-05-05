from django.shortcuts import render
from .cart import Cart
def CartDetail(request):
    cart = Cart(request)
    print(cart.__dict__)
    print(cart.__getattribute__)

    context = {
        'cart':cart
    }
    return render(request,'cart.html', context)
