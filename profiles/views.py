from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from classes.models import Classes


@login_required
def profile(request):
    """ Display user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    classes = Classes.objects.all()

    username = profile.user.username

    classes_list = []

    for c in classes:
        for user in c.attending:
            if user == username:
                class_info = [c.name, c.class_day, c.class_time]
                classes_list.append(class_info)


    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = "checkout/checkout_success.html"
    context = {
        'order': order,
        'from_profile': True
    }

    return render(request, template, context)
