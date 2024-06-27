from django.db import models

# Create your models here.
class banner(models.Model):
        image = models.FileField(max_length=100,upload_to='secbanner/',null=True)