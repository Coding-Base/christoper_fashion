from django.urls import path
from .views import BlogListCreateView

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
]
