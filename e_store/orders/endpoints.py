from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from .models import Order
from .serializers import OrderSerializer


class OrderView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            order_id = serializer.data.get('id')
            order = Order.objects.get(id=order_id)
            order.save()
            return Response({'data': 'OK'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class DeleteOrderView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        order = Order.objects.get(id=kwargs['pk'])
        order.delete()
        return Response({'data': 'order is canceled'})
