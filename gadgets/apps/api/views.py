from django.shortcuts import render
from apps.store.models import *
from .serializers import ProductSerializer
from rest_framework import generics

class ProductViewSets(generics.ListAPIView):
    
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        id__gte = self.request.query_params.get("id__gte")
        id__lte = self.request.query_params.get("id__lte")
        if (id__lte and id__gte) is not None:
            queryset = queryset.filter(id__gte=id__gte, id__lte=id__lte)[::-1]
        return queryset
            
