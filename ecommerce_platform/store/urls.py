from django.urls import path
from .import views

urlpatterns = [
    path('products/',views.ListCreateProducts.as_view(),name='ListProducts'),
    path('products/<int:id>',views.RetrieveProduct.as_view(),name='ListProduct')
]