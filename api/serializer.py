from rest_framework import routers, serializers, viewsets
from .models import Product, Price


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    #product_price = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'code', 'size', 'color', 'slug', 'price']
