'''from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]'''


from django.urls import path
from .views import ViewCartView, AddToCartView, RemoveFromCartView

app_name = 'cart'

urlpatterns = [
    path('cart/', ViewCartView.as_view(), name='view_cart'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]
