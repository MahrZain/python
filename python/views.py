from django.shortcuts import render
from products.models import products
from carousel.models import carousel
#Create Views Here
def home(request):
    pr_data = products.objects.all()
    car_data = carousel.objects.all()
    data = {
        "products": pr_data,
        "carousel": car_data
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
