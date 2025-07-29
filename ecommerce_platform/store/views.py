from rest_framework.generics import ListCreateAPIView,RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response


class ListCreateProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    