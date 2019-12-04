from django.urls import path
from .views import ProductListView, ProductView, ProductPriceRangeView
urlpatterns = [
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('product/<pk>', ProductView.as_view(), name='product-list'),
    path('price/<first>/<last>', ProductPriceRangeView.as_view(), name='product-list'),
]
