from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions

from .models import Comment, Rating
from .serializers import CommentSerializer, RatingSerializer


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class RatingListCreateAPIView(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (permissions.IsAuthenticated,)
