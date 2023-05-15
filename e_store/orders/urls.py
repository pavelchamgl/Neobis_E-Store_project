from django.urls import path

from .endpoints import OrderView, DeleteOrderView


urlpatterns = [
    path('', OrderView.as_view(), name='order'),
    path('<int:pk>/delete/', DeleteOrderView.as_view(), name='delete'),
]
