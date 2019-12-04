from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class ProductListView(APIView):
    @staticmethod
    def get(request):
        product_list = Product.objects.all()
        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductView(APIView):
    @staticmethod
    def get(request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def patch(request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductPriceRangeView(APIView):
    @staticmethod
    def get(request, first, last):
        products = Product.objects.filter(price__price__gt=first, price__price__lte=last)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
