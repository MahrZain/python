from django.http import HttpRequest
from django.shortcuts import render
from django.template import loader

def home():
    return render(request , 'index.html')