from django.shortcuts import render

# Create your views here.


def reg(request):
    return render(request,'registration.html')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')