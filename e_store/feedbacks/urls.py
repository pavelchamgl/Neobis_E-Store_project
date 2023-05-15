from django.urls import path

from .endpoints import CommentListCreateAPIView, RatingListCreateAPIView


urlpatterns = [
    path('comment', CommentListCreateAPIView.as_view(), name='comment'),
    path('rating/', RatingListCreateAPIView.as_view(), name='rating'),
]