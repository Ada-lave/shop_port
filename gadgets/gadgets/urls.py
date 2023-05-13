"""
URL configuration for gadgets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from apps.store.api import ApiAddToCart, ApiRemoveCart, ApiCheckout
from apps.coupon.api import ApiCanUse
from apps.core.views import *
from apps.store.views import *
from apps.cart.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", frontpage, name='frontpage'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('cart/', CartDetail, name='cart'),


    # API
    path('api/AddToCard/', ApiAddToCart, name='ApiAddToCart'),
    path('api/RemoveCart/', ApiRemoveCart),
    path('api/checkout/', ApiCheckout),
    path('api/checkcoupon/', ApiCanUse),


    path("<slug:category_slug>/", category_detail, name='category_detail'),
    path("<slug:category_slug>/<slug:slug>/",
         product_detail, name='product_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
