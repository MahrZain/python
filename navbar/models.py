from django.db import models

# Create your models here.

class nav(models.Model):
    menu = models.CharField(max_length=100, null=True)
    url = models.URLField(max_length=200)
    # order = models.PositiveIntegerField(default=0)
    
# class Meta:
#         ordering = ['order']