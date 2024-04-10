from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import OrderModel, OrderItem, CustomerData, DeliverData


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)
        # loop through the orders and add the price value, check if order is not shipped
        today_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price
            #if not order.is_shipped:
            today_orders.append(order),
        customer_data = CustomerData.objects.filter(order__in=orders)
        combined_instances = zip(orders, customer_data)
        # pass total number of orders and total revenue into template
        context = {
            'orders': today_orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders),
            'combined_instances': combined_instances,
        }

        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()


class OrderDetails(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order_items = order.items.all()
        elements = OrderItem.objects.filter(order_id=pk)
        customer = CustomerData.objects.get(order_id=pk)
        deliver = DeliverData.objects.get(order_id=pk)
        context = {
            'order': order,
            'order_items': order_items,
            'elements': elements,
            'customer': customer,
            'deliver': deliver,
        }

        return render(request, 'restaurant/order-details.html', context)

    def post(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)
        order_items = order.items.all()
        elements = OrderItem.objects.filter(order_id=pk)
        customer = CustomerData.objects.get(order_id=pk)
        deliver = DeliverData.objects.get(order_id=pk)
        order.is_shipped = True
        order.save()

        context = {
            'order': order,
            'order_items': order_items,
            'elements': elements,
            'customer': customer,
            'deliver': deliver,
        }

        return render(request, 'restaurant/order-details.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()