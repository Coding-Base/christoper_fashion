from rest_framework import serializers
from .models import Product, Category
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
     image = serializers.SerializerMethodField()
     author = serializers.StringRelatedField()
     def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

     class Meta:
        model = Blog
        fields = ['id', 'title', 'content',  "author", 'image', 'created_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
