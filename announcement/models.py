from django.db import models

# Create your models here.
class Announcement(models.Model):
    message = models.CharField(max_length=200, null=True , blank=True)
    buy_now = models.URLField(null=True , blank=True)