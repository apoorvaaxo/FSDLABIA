from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def current_datetime(request):
    now=datetime.now()
    html=f"<html><body>Current date and time is: {now}</body></html>"
    return HttpResponse(html)
    
    
    
    