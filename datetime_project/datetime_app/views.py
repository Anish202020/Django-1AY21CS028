from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone


def current_datetime(request):
    now = timezone.now()
    html = "<html><body>Current date and time: {}</body></html>".format(now)
    return HttpResponse(html)