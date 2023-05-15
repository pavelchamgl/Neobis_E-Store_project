from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, default=0, read_only=True)
    total_sum = serializers.SerializerMethodField()
    OrderItem = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'date_create', 'status', 'total_price', 'total_sum',
                  'city', 'street', 'house', 'pay_method', 'OrderItem']

    def create(self, validated_data):
        order_item_data = validated_data.pop('OrderItem')
        order = Order.objects.create(**validated_data)
        self.get_total_sum(order)

        for item in order_item_data:
            drop_id = item.pop('id')
            OrderItem.objects.create(order=order, **item)
        return order

    def get_total_sum(self, obj):
        total_sum = 0
        for item in obj.OrderItem.all():
            total_sum += item.product.price * item.quantity
        obj.total_price = total_sum
        obj.save()
        return total_sum
