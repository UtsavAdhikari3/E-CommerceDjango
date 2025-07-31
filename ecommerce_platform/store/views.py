from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from rest_framework.views import APIView
from .models import Product,CartItem,Cart
from .serializers import ProductSerializer,CartItemSerializer
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User



class ListCreateProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    

class AddProductToCart(APIView):
    permission_classes = [permissions.IsAuthenticated]
    