from django.shortcuts import render


def index(request):
    """ A view to return the home page"""
    template = 'home/index.html'

    return render(request, template)


def about_us(request):
    """ A view to return the about_us page"""
    template = 'home/about_us.html'

    return render(request, template)
