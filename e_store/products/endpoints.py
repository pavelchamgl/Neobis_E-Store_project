from rest_framework.generics import ListAPIView, RetrieveAPIView

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


class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return Product.objects.filter(id=product_id)
