from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from store.models import Product

# Create your views here.


def view_bag(request):
    """ A  view that renders that shopping bag """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    A view that gets an item, checks if it has size and adds
    the item to the shopping bag based on size or not size
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # create or get session variable
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'''Updated {size.upper()} {product.name},
                    quantity to {bag[item_id]["items_by_size"][size]}''')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'''Added {size.upper()} {product.name},
                    to your bag''')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            # if item in bag update quanity
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            # if item not in bag add to bag
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    # overwrite session varaible with updated version of bag
    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    This view updates the quantity of an item in the bag.
    Changes how items are handled based on size.
    If item quanity set to zero item is removed from bag
    """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # create or get session variable
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'''Updated {size.upper()} {product.name},
                 quantity to {bag[item_id]["items_by_size"][size]}''')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f'''Removed {size.upper()},
                    {product.name} from your bag''')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from bag')
    # overwrite session varaible with updated version of bag
    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):

    try:
        product = Product.objects.get(pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        # create or get session variable
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(
                    request, f'''Removed {size.upper()},
                    {product.name} from your bag''')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from bag')
        # overwrite session varaible with updated version of bag
        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
