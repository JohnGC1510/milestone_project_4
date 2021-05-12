from django.shortcuts import render


def view_bag(request):
    """ A  view that renders that shopping bag """
    return render(request, 'bag/bag.html')
