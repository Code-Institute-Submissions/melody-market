from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_items(request):
    """ A view to return the items with the sorting and searching functionalities """

    items = Product.objects.all()
    query = None
    category = None

    if request.GET:

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

    context = {
        'products': items,
        'search_term': query,
        'current_categories': category,
    }

    return render(request, 'products/items.html', context)

def item_details(request, product_id):
    """ A view to return the item details """

    item = get_object_or_404(Product, pk=product_id)

    context = {
        'product': item,
    }

    return render(request, 'products/item_details.html', context)