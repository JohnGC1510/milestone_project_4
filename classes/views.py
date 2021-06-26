from django.shortcuts import render, redirect, reverse


def classes(request):
    """ A view to return the about_us page"""

    if request.method == 'POST':
        return redirect(reverse('classes'))

    template = 'classes/classes.html'

    return render(request, template)
