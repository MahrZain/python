from django.shortcuts import render

#Create Views Here
def home(request):
    return render(request, 'index.html')
