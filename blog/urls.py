from django.urls import path
from .views import index, get_blogs_form_category

urlpatterns=[
    path("", index, name="blog"),
    path("categoria/<str:pk>", get_blogs_form_category, name="blog_form_category")
]
