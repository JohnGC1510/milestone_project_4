from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def store_home(request):
    """ A view to return the store page"""
    template = 'store/store_home.html'
    query = None
    categories = None

    products = Product.objects.all()

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """ A view to show the individial product details """
    template = 'store/product_detail.html'

    product = get_object_or_404(Product, pk=product_id)

    context ={
        'product': product,
    }

    return render(request, template, context)
