from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    in_stock = models.BooleanField()
    quantity = models.IntegerField(validators=[MaxValueValidator(1000),MinValueValidator(1)])
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True,null=True)