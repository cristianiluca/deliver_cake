'''from django.shortcuts import render, redirect, HttpResponse
from .models import Product, CartItem
from customer.models import MenuItem'''

from django.shortcuts import render, redirect
from django.views import View
from customer.models import MenuItem, Cart
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages


class ViewCartView(UserPassesTestMixin, LoginRequiredMixin, View):
    template_name = 'cart.html'

    def get(self, request):
        cart_items = Cart.objects.all()
        total_price = round(sum(item.product.price * item.quantity for item in cart_items), 2)
        for cart_item in cart_items:
            cart_item.total = cart_item.total_price_item()
        context = {
            'cart_items': cart_items,
            'total_price': total_price,
        }

        return render(request, self.template_name, context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class AddToCartView(UserPassesTestMixin, LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = MenuItem.objects.get(id=product_id)
        cart_item, created = Cart.objects.get_or_create(product=product)
        cart_item.quantity = request.POST.get('cantitate')
        cart_item.save()
        return redirect('cart:view_cart')

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class RemoveFromCartView(UserPassesTestMixin, LoginRequiredMixin, View):
    def get(self, request, item_id):
        cart_item = Cart.objects.get(id=item_id)
        cart_item.delete()
        return redirect('cart:view_cart')

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()



'''def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    product = MenuItem.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    cart_item.quantity = request.POST.get('cantitate')
    cart_item.save()
    return redirect('cart:view_cart')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
'''

