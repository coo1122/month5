from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import CategorySerializer, CategoryDetailSerializer, ProductSerializer, ProductDetailSerializer, ReviewSerializer, ReviewDetailSerializer

@api_view(['GET'])
def category_detail_api_view(request,id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = CategorySerializer(category).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def category_list_api_view(request):
    shop = Category.objects.all()
    data = CategorySerializer(shop, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_detail_api_view(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductSerializer(product).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def product_list_api_view(request):
    shop = Category.objects.all()
    data = CategorySerializer(shop, many=True).data
    return Response(data=data)

@api_view(['GET'])
def review_detail_api_view(request,id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review).data
    return Response(data=data)

@api_view(http_method_names=['GET'])
def review_list_api_view(request):
    shop = Review.objects.all()
    data = ReviewSerializer(shop, many=True).data
    return Response(data=data)