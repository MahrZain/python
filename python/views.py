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
    return render(request, "contact.html")


def savcontact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        if not email or not email or not phone or not message:
            return render(request, "contact.html")
        else:
            sav = Contact(name=name, email=email, phone=phone, message=message)
            sav.save()
    return render(request, "contact.html")


def search(request, mytitle):
    query = request.GET.get("searched")
    products.objects.filter(title=mytitle)
    return render(request, "")


def about(request):
    nav_bar = nav.objects.all()
    data = {
        "nav": nav_bar,
    }
    return render(request, "about.html", data)


def login(request):
    return render(request, "login.html")

def loginUser(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def registerUser(request):
    fname = request.POST['name']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    print(fname, lname, email, password)
    return render(request, "register.html")


def viewproducts(request, myid):
    product = products.objects.filter(id=myid)
    return render(request, "products.html", {"product": product[0]})


def faq(request):
    return render(request, "faq.html")


def search(request):
    result = request.GET['query']
    fresult = products.objects.filter(title__icontains = result)
    return render(request, "search.html",{"fresult":fresult})
