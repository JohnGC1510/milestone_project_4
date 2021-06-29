from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order
from classes.models import Classes
from store.models import Product, Favourite


@login_required
def profile(request):
    """ Display user's profile """

    profile = get_object_or_404(UserProfile, user=request.user)
    class_list= []
    fav = None
    fave_products = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    else:
        form = UserProfileForm(instance=profile)
    
    all_classes = Classes.objects.all()

    for c in all_classes:
        for attendee in c.attending:
            if str(request.user) == str(attendee):
                class_info = [c.name, c.class_day, c.class_time]
                class_list.append(class_info)

    try:
        favourites = Favourite.objects.get(userid=request.user)
        fav = list(favourites.product_ids)
    except Favourite.DoesNotExist:
        favourites = Favourite(userid=request.user)
        fav = list(favourites.product_ids)

    fave_products = Product.objects.filter(id__in=fav)

    template = 'profiles/profile.html'

    context = {
        'profile': profile,
        'form': form,
        'class_list': class_list,
        'on_profile_page': True,
        'fave_products': fave_products
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
