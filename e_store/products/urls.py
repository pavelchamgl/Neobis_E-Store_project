from django.urls import path

from .endpoints import ProductCategoryListAPIView, ProductsByCategoryListAPIView, ProductDetailView

urlpatterns = [
    path('categories/', ProductCategoryListAPIView.as_view(), name='products_category'),
    path('categories/<int:category_id>/products/', ProductsByCategoryListAPIView.as_view(), name='products_by_category'),
    path('categories/<int:products_id>/products/', ProductDetailView.as_view(), name='products'),
]