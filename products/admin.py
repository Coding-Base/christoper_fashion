from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Category
from .models import Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display =('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    
admin.site.register(Product)
admin.site.register(Category)