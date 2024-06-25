from django.db import models
from static import *
# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    price = models.IntegerField()
    category = models.CharField(max_length=60)
    total_amount_products = models.IntegerField()
    rating = models.IntegerField()