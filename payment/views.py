from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def payment(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty...")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'payment/payment.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)