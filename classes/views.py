from django.shortcuts import render, redirect, reverse
from .models import Classes


def classes(request):
    """ A view to return the about_us page"""

    classes = Classes.objects.all()

    template = 'classes/classes.html'

    context = {
        'classes': classes
    }

    return render(request, template, context)