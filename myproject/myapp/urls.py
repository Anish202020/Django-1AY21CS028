# myapp/urls.py
from django.urls import path
from .views import my_view

urlpatterns = [
    path('my-page/', my_view, name='my_page'),
]
