import json
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.db.models import Q
from django.core.mail import send_mail
from .models import MenuItem, Category, OrderModel, Cart, OrderItem, CustomerData, DeliverData
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from cart.forms import InputQuantity
from django.contrib import messages
from datetime import date


class Index(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class About(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class Order(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        items = Cart.objects.all()
        context = {
            'items': items,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        phone = request.POST.get('phone')
        cake_text = request.POST.get('cake_text')
        deliver_date = request.POST.get('deliver_date')
        deliver_time = request.POST.get('deliver_time')
        deliver_name = request.POST.get('deliver_name')
        deliver_email = request.POST.get('deliver_email')
        deliver_street = request.POST.get('deliver_street')
        deliver_city = request.POST.get('deliver_city')
        deliver_state = request.POST.get('deliver_state')
        deliver_zip_code = request.POST.get('deliver_zip')
        deliver_phone = request.POST.get('deliver_phone')

        order_items = {
            'items': []
        }

        cart_items = Cart.objects.all()
        items = [item.product_id for item in cart_items]

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=item)
            quant = Cart.objects.get(product_id=item)

            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
                'quantity': quant.quantity,
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']*item['quantity']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price
        )
        order.items.add(*item_ids)

        if not deliver_date:
            deliver_date = date.today()

        customer = CustomerData.objects.create(
            order=order,
            name=name if name else None,
            email=email if email else None,
            street=street if street else None,
            city=city if city else None,
            state=state if state else None,
            zip_code=zip_code if zip_code else None,
            phone=phone if phone else None,
            deliver_date=deliver_date,
            deliver_time=deliver_time if deliver_time else None,
            cake_text=cake_text if cake_text else None,
        )

        if not deliver_name:
            deliver_name = name
        if not deliver_email:
            deliver_email = email
        if not deliver_street:
            deliver_street = street
        if not deliver_city:
            deliver_city = city
        if not deliver_state:
            deliver_state = state
        if not deliver_zip_code:
            deliver_zip_code = zip_code
        if not deliver_phone:
            deliver_phone = phone

        deliver = DeliverData.objects.create(
            order=order,
            deliver_name=deliver_name,
            deliver_email=deliver_email,
            deliver_street=deliver_street,
            deliver_city=deliver_city,
            deliver_state=deliver_state,
            deliver_zip_code=deliver_zip_code,
            deliver_phone=deliver_phone,
        )
        for cart_item in cart_items:
            OrderItem.objects.create(order=order, name=cart_item.product, quantity=cart_item.quantity)

        # After everything is done, send confirmation email to the user
        body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
                f'Your total: {price}\n'
                'Thank you again for your order!')

        send_mail(
            'Thank You For Your Order!',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )

        Cart.objects.all().delete()

        return redirect('order-confirmation', pk=order.pk)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class OrderConfirmation(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class OrderPayConfirmation(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class Menu(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class MenuSearch(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class MenuDetail(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, id, *args, **kwargs):
        product = MenuItem.objects.get(id=id)
        if request.method == 'POST':
            form = InputQuantity(request.POST)
            if form.is_valid():
                cantitate = form.cleaned_data.get('cantitate')
                return HttpResponse("Form value received: " + cantitate)
        else:
            form = InputQuantity
        context = {
            'product': product,
            'form': form,
        }
        return render(request, 'customer/menu_detail.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


