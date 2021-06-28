from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Classes

import json

@csrf_exempt
def classes(request):
    """ A view to return the about_us page"""
    user = request.user
    classes_attending = []
    message = ""

    if request.is_ajax and request.method == "POST":
        curr_class = Classes.objects.get(pk=request.POST.get("class_pk"))
    
        if user.username in curr_class.attending:
            curr_class.attending.remove(user.username)
            message = "You have been removed from the class"
        elif len(curr_class.attending) < curr_class.max_attending:
            curr_class.attending.append(user.username)
            message = "You have subscribed to the class"
        elif len(curr_class.attending) >= curr_class.max_attending:
            message = "The class is currently full please try another class"
                
        curr_class.save()

        return HttpResponse(json.dumps(
            {'message': message}), content_type="application/json")

    classes = Classes.objects.all()
    classes = classes.order_by('pk')

    for c in classes:
        if user.username in c.attending:
            classes_attending.append(c.pk)

    template = 'classes/classes.html'

    context = {
        'classes': classes,
        'user_classes': classes_attending
    }

    return render(request, template, context)
