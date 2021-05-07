from django.shortcuts import render
from .models import Product


def store_home(request):
    """ A view to return the home page"""
    template = 'store/store_home.html'

    products = Product.objects.all()

    context ={
        'products': products,
    }

    return render(request, template, context)
