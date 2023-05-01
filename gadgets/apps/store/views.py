from django.shortcuts import get_object_or_404, render
from .models import *
def product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)

    context = {
        'product':product
    }

    return render(request, 'productDetail.html',context)


def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.all()

    context = {
        'category':category,
        'products': products
    }

    return render(request, 'categoryDetail.html', context)

