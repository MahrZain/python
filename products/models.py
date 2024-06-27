from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=120)
    price = models.IntegerField()
    category = models.CharField(max_length=60)
    total_amount_products = models.IntegerField()
    sale = models.IntegerField(blank=True , null=True)
    image = models.FileField(max_length=100, upload_to="images/",null=True)