from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category, Blog
from .serializers import ProductSerializer, CategorySerializer, BlogSerializer
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
import requests

# ViewSets
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_context(self):
        return {'request': self.request}


# API Views
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer

# Payment API
SELAR_API_KEY = settings.SELAR_API_KEY

@api_view(['POST'])
def create_payment_link(request):
    try:
        product_id = request.data.get('product_id')
        email = "osimigodsgiftgbubemi@gmail.com"  # Hardcoded email for now
        print("Product ID:", product_id)
        print("Email:", email)

        if not product_id or not email:
            return JsonResponse({"error": "Missing product_id or email"}, status=400)
        
        product = Product.objects.get(id=product_id)

        # Convert Decimal to float
        payment_data = {
            "amount": float(product.price),  # Ensure JSON serializable
            "currency": "NGN",
            "order_id": f"order-{product.id}",  # Unique order ID
            "email": email,
            "callback_url": "http://localhost:3000/",  # Success redirect
            "cancel_url": "http://localhost:3000/",  # Failure redirect
            "description": product.name,  # Product description
        }

        headers = {
            "Authorization": f"Bearer {SELAR_API_KEY}",
            "Content-Type": "application/json",
        }

        response = requests.post("https://selar.co/m/osimigbubemigodsgift", json=payment_data, headers=headers)
        print("Payment Gateway Response:", response.text)
       
        if response.status_code == 201:
            payment_link = response.json().get('data', {}).get('payment_url', '')
            return Response({"payment_url": payment_link}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Failed to create payment link"}, status=response.status_code)

    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
