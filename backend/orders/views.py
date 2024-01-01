from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer
from payments.views import create_order_payment


class OrderViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self) -> dict:
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def perform_create(self, serializer):
        instance = serializer.save()
        create_order_payment(instance, serializer.context.get("request"))


class OrderItemViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = OrderItem.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderItemSerializer
