from django.shortcuts import render
from products.models import products
from carousel.models import carousel
from banner.models import banner
#Create Views Here
def home(request):
    pr_data = products.objects.all()
    car_data = carousel.objects.all()
    sec_banner = banner.objects.all()
    data = {
        "products": pr_data,
        "carousel": car_data,
        "SB": sec_banner
    }
    return render(request, 'index.html', data)
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
def contact(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request , 'faq.html')
