from django import template


register = template.Library()

@register.filter(name='return_subtotal')
def return_subtotal(price, quantity):
    return price * quantity