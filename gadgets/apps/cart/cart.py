from django.conf import settings
from apps.store.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
    
    def __iter__(self):
        product_ids = self.cart.keys()

        product_clean_ids = []

        for p in product_ids:
            product_clean_ids.append(p)
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
        
        for item in self.cart.values():
    
            item['total_price'] = float(item['price']) * int(item['quantity'])

            yield item
        
        
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def remove(self, product_id):
        print('rm')
        if product_id in self.cart:
            print('test rm')
            del self.cart[product_id]
            self.save()

    
    def add(self, product, quantity, update_q=False):
        product_id = str(product.id)
        price = product.price
        print(f"prod id {product_id}")

        if product_id not in self.cart:
            print('test 1')
            self.cart[product_id] = {'quantity':0, 'price':price, 'id':product_id}

        if update_q is False:
            self.cart[product_id]['quantity'] = 1
        
        elif update_q == 'inc':
            self.cart[product_id]['quantity'] -= 1
        else:
            print('test 2')
            self.cart[product_id]['quantity'] += 1
        
        self.save()
    
    def save(self):
        
        print('save')
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
        
    def TotalLenght(self):
        return sum(int(item['quantity']) for item in self.cart.values())
    
    def TotalPrice(self):
        try:
            return sum((item['total_price'] for item in self.cart.values()))
        except Exception:
            return 0