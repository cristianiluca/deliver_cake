from django.contrib import admin
from .models import MenuItem, Category, OrderModel, Cart, OrderItem

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(Cart)
admin.site.register(OrderItem)
