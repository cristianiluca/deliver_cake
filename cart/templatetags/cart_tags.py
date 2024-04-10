# cart_tags.py

from django import template
from customer.models import Cart  # Import your CartItem model

register = template.Library()

@register.simple_tag
def cart_item_count():
    return Cart.objects.count()
