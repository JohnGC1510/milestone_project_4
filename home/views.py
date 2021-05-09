from django.shortcuts import render
from store.models import Product

import random

def index(request):
    """ A view to return the home page"""

    products = list(Product.objects.all())

    products = random.sample(products, 7)

    template = 'home/index.html'

    context = {
        'products': products,
    }

    return render(request, template, context)


def about_us(request):
    """ A view to return the about_us page"""
    template = 'home/about_us.html'

    return render(request, template)
