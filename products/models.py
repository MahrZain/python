from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    price = models.IntegerField()
    category = models.TextField(max_length=60)