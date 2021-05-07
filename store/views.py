from django.shortcuts import render


def store_home(request):
    """ A view to return the home page"""
    template = 'store/store_home.html'

    return render(request, template)
