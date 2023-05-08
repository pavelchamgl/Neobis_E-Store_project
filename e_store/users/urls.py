from django.urls import path, include, re_path

from .endpoints import UserProfileListAPIView

urlpatterns = [
    re_path('auth/', include('djoser.urls')),
    re_path('auth/', include('djoser.urls.jwt')),
    path('auth/profile/', UserProfileListAPIView.as_view(), name='profile'),
]
