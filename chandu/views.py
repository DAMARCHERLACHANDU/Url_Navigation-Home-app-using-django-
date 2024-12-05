from django.shortcuts import render

# Create your views here.

def dress(request):
    return render(request,'shop.html')

def eating(request):
    return render(request,'chicken.html')