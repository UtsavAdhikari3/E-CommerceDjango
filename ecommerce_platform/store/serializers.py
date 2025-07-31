from rest_framework import serializers
from .models import Product, CartItem, Cart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['products','quantity','subtotal']

    def get_subtotal(self,obj):
        return obj.quantity * obj.products.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['items', 'total']

    def get_total(self, obj):
        return sum(item.products.price * item.quantity for item in obj.items.all())

