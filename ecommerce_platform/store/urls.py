from django.urls import path
from .import views

urlpatterns = [
    path('product/',views.ListCreateProducts.as_view(),name='ListProducts'),
    path('product/<int:pk>',views.RetrieveProduct.as_view(),name='ListProduct')
]