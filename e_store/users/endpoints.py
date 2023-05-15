from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .models import User
from .serializers import UserProfileSerializer


class UserProfileListAPIView(ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
