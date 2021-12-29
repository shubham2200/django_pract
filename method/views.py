from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse


# Create your views here.

def home(request):
    return render(request,'home.html')

def save_data(request):
    if request.method == "POST":
        dict1=request.POST.get('my_data')
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = user_data()
        user.name = name
        user.email= email
        user.password = password 
        user.save()
        return JsonResponse({})
        
        