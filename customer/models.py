from django.db import models
from datetime import date
from django.utils import timezone


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(MenuItem, related_name='order', blank=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.items}'


class CustomerData(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    deliver_date = models.DateField(default=date.today, blank=True, null=True)
    deliver_time = models.TimeField(default=timezone.now, blank=True, null=True)
    cake_text = models.TextField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return f'{self.order} - {self.name}'


class DeliverData(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    deliver_name = models.CharField(max_length=50, blank=True, null=True)
    deliver_email = models.CharField(max_length=50, blank=True, null=True)
    deliver_street = models.CharField(max_length=50, blank=True, null=True)
    deliver_city = models.CharField(max_length=50, blank=True, null=True)
    deliver_state = models.CharField(max_length=15, blank=True, null=True)
    deliver_zip_code = models.IntegerField(blank=True, null=True)
    deliver_phone = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return f'{self.order} - {self.name}'


class Cart(models.Model):
    product = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    def total_price_item(self):
        return self.product.price * self.quantity


class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    name = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.order} - {self.name} x {self.quantity}'

    def print_details(self):
        print(f"Order: {self.order}")
        print(f"Item: {self.name.name}")
        print(f"Quantity: {self.quantity}")
