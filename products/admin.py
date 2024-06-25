from django.contrib import admin
from .models import products
# Register your models here.
class productsAdmin(admin.ModelAdmin):
    list_display = ['title','description','price','category']
    
admin.site.register(products,productsAdmin)