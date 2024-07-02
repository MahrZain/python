from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()
    message = models.TextField()