# myapp/views.py
from django.shortcuts import render

def my_view(request):
    return render(request, 'myapp/my_template.html')
