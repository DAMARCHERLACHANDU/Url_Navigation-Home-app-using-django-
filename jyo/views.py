from django.shortcuts import render

# Create your views here.

def biryani(request):
    return render(request,'food.html')


def come(request):
    return render(request,'home.html')
