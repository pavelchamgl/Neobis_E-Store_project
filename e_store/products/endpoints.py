from django.views.generic import DetailView
from rest_framework import permissions, status, viewsets, request
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .serializers import ProductCategorySerializer, ProductSerializer
from .models import ProductCategory, Product


class ProductCategoryListAPIView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class ProductsByCategoryListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(APIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Product.objects.filter(product_id=product_id)
