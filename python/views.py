from django.shortcuts import render
from products.models import products
#Create Views Here
def home(request):
    pr_data = products.objects.all()
    data = {
        "products": pr_data
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
