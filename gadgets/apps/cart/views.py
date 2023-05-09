from django.shortcuts import render
from .cart import Cart


def CartDetail(request):
    cart = Cart(request)
    productstr = ''

    for item in cart:
        product = item['product']
        b = "{'id':'%s', 'title':'%s', 'price':'%s','quantity':'%s'}" % (product.id, product.title, product.price, item['quantity'])

        productstr += b
    print(productstr)
    context = {
        'cart':cart,
        'productstr': productstr
    }
    return render(request,'cart.html', context)
