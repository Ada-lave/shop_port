from django.shortcuts import render
from .cart import Cart


def CartDetail(request):
    cart = Cart(request)
    productstr = []

    for item in cart:
        product = item['product']
        b = {'id':product.id, 'title':product.title, 'price':product.price,'quantity':item['quantity'],'total_price':item['total_price']}

        productstr.append(b)
    print(productstr)
    context = {
        'cart':cart,
        'productstr': productstr
    }
    return render(request,'cart.html', context)
