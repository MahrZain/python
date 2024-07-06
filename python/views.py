from django.shortcuts import render
from products.models import products
from carousel.models import carousel
from banner.models import banner
from logo.models import limage
from announcement.models import Announcement
from navbar.models import nav
from contact.models import Contact


# Create Views Here
def home(request):
    pr_data = products.objects.all()
    car_data = carousel.objects.all()
    sec_banner = banner.objects.all()
    latest_logo = limage.objects.all()
    msg_text = Announcement.objects.all()
    nav_bar = nav.objects.all()
    data = {
        "products": pr_data,
        "carousel": car_data,
        "SB": sec_banner,
        "logo": latest_logo,
        "message": msg_text,
        "nav": nav_bar,
    }
    return render(request, "index.html", data)

def contact(request):
    return render(request, 'contact.html')
def savcontact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        sav = Contact(name=name, email=email, phone=phone, message=message)
        sav.save()
    return render(request, 'contact.html')
def about(request):
    return render(request, "about.html")


def login(request):
    return render(request, "login.html")




def faq(request):
    return render(request, "faq.html")
