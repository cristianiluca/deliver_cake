from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from cake_api import views
from customer.views import Index, About, Order, OrderConfirmation, OrderPayConfirmation, Menu, MenuSearch, MenuDetail

app_name = 'deliver'

router = routers.DefaultRouter()
router.register(r'orders', views.OrderModelViewSet, basename='orders')
router.register(r'orderitem', views.OrderItemViewSet, basename='orderitem')
router.register(r'customerdata', views.CustomerDataViewSet, basename='customerdata')
router.register(r'deliverdata', views.DeliverDataViewSet, basename='deliverdata')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('', include('cart.urls', namespace='cart')),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('menu/', Menu.as_view(), name='menu'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('menu-detail/<int:id>/', MenuDetail.as_view(), name='menu-detail'),
    path('order/', Order.as_view(), name='order'),
    path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),
         name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),
         name='payment-confirmation'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


