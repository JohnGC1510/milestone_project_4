from django.shortcuts import render


def classes(request):
    """ A view to return the about_us page"""
    template = 'classes/classes.html'

    return render(request, template)
