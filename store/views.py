from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Favourite
from .forms import ProductForm
from profiles.models import UserProfile


def store_home(request):
    """
    A view to retreive the products from the db
    and filter them when a request is made from
    the front end
    """
    template = 'store/store_home.html'
    query = None
    categories = None
    sort = None
    direction = None

    products = Product.objects.all()

    products = products.exclude(category=11)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'  # sort by name instead of id
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """ A view to show the individial product details """
    template = 'store/product_detail.html'
    fav_items = None

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        favs = Favourite.objects.get_or_create(userid=request.user)
        if favs[0].product_ids:
            fav_items = list(favs[0].product_ids)

    context = {
        'product': product,
        'fav_items': fav_items,
    }

    return render(request, template, context)


def membership(request):

    profile = None
    purchase = False

    if request.user.is_authenticated:
        purchase = True
        profile = get_object_or_404(UserProfile, user=request.user)

    member_types = Product.objects.filter(category=11)

    template = 'store/membership.html'

    context = {
        'member_types': member_types,
        'purchase': purchase,
        'profile': profile
    }

    return render(request, template, context)


@login_required
def add_favourite(request, product_id):

    fav = Favourite.objects.get_or_create(userid=request.user)
    if product_id in fav[0].product_ids:
        fav[0].product_ids.remove(product_id)
        fav[0].save()
        messages.success(request, "Product removed from favoruties")
    else:
        fav[0].product_ids.append(product_id)
        fav[0].save()
        messages.success(request, "Product added to favoruties")

        return redirect(reverse('product_detail', args=[product_id]))


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'store/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                            request,
                            'Failed to update product. Ensure form is valid.'
                        )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'store/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('store'))
