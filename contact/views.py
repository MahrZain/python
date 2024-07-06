from django.shortcuts import render, redirect
from .models import Contact


def contact(request):
    return render(request, 'contact.html')
    
def savcontact(request):
    pass
