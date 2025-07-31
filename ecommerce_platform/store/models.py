from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    in_stock = models.BooleanField()
    quantity = models.IntegerField(validators=[MaxValueValidator(1000),MinValueValidator(1)])
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])