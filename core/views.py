from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'landing.html')


def products(request):
    return render(request, 'core/products.html')


def detail(request):
    return render(request, 'core/product_details.html')
