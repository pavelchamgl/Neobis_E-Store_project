from django.urls import path

from .endpoints import ProductCategoryListAPIView, ProductsByCategoryListAPIView, ProductDetailView

urlpatterns = [
    path('', ProductCategoryListAPIView.as_view(), name='products_category'),
    path('<int:category_id>/category/', ProductsByCategoryListAPIView.as_view(), name='products_by_category'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
]