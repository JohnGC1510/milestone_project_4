from django.shortcuts import render


def profile(request):
    """ A view to return the profile page"""

    template = 'profile/profile.html'

    context = {}

    return render(request, template, context)
