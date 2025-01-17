from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime, timedelta

def current_datetime(request):
    now = datetime.now()
    four_hours_ahead = now + timedelta(hours=4)
    four_hours_before = now - timedelta(hours=4)
    
    html = "<html><body>"
    html += "Current date and time: {}<br>".format(now)
    html += "Date and time four hours ahead: {}<br>".format(four_hours_ahead)
    html += "Date and time four hours before: {}<br>".format(four_hours_before)
    html += "</body></html>"
    
    return HttpResponse(html)

