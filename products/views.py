from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Product, Category, Condition, Sale

from .forms import ProductForm

# Create your views here.

def all_items(request):
    """ A view to return the items with the sorting and searching functionalities """

    items = Product.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please input the item you are looking for")
                return redirect(reverse('items'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            items = items.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': items,
        'search_term': query,
        'current_categories': category,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/items.html', context)

def item_condition(request, product_id):

    """ A view to show if the item is used """

    condition = None

    if 'condition' in request.GET:
            conditions = request.GET['items']
            items = items.filter(condition__name__in=conditions)
            conditions = Condition.objects.filter(name__in=conditions)

    context = {
        'products': items,
        'conditions': conditions,
    }
    
    return render(request, 'products/second_hand.html')

def item_sale(request):
    
    """ A view to show if the item is on sale """

    items = Product.objects.all()
    sale = Sale.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'products/sale.html', context)

def item_details(request, product_id):

    """ A view to return the item details """

    item = get_object_or_404(Product, pk=product_id)

    context = {
        'product': item,
    }

    return render(request, 'products/item_details.html', context)

def add_item(request):
    
    """ Allows users adding items to the store """
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not permitted to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'New item added successfully!')
            return redirect(reverse('add_item'))
        else:
            messages.error(request, 'Failed to add item. Please check the form.')
    else:
        form = ProductForm()
        
    template = 'products/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_item(request, product_id):

    """ Allows users adding items in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not permitted to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully updated store item!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update item. Please check the form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_item.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_item(request, product_id):

    """ Allows users deleting items from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not permitted to do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'You have deleted the item!')
    return redirect(reverse('items'))

