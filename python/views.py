from django.shortcuts import render
from products.models import products
from carousel.models import carousel
from banner.models import banner
from logo.models import limage
from announcement.models import Announcement


# Create Views Here
def home(request):
    pr_data = products.objects.all()
    car_data = carousel.objects.all()
    sec_banner = banner.objects.all()
    latest_logo = limage.objects.all()
    msg_text = Announcement.objects.all()
    # buy_link = buy_now.objects.all()
    data = {
        "products": pr_data,
        "carousel": car_data,
        "SB": sec_banner,
        "logo": latest_logo,
        "message": msg_text,
        # "buy": buy_link,
    }
    return render(request, "index.html", data)


def about(request):
    return render(request, "about.html")


def login(request):
    return render(request, "login.html")


def contact(request):
    return render(request, "contact.html")


def faq(request):
    return render(request, "faq.html")
