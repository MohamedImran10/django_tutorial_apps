from django.shortcuts import render, HttpResponse
from django.http import Http404
from datetime import datetime, timedelta

def current_date(request):
    now = datetime.now().date()
    html = f"<html><body><font color='magenta'>Today's date is {now}.</font></body></html>"
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.now()
    html = f"<html><body><font color='red'>It is now {now}.</font></body></html>"
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.now() + timedelta(hours=offset)
    html = f"<html><body><font color='blue'>In {offset} hours, it will be {dt}.</font></body></html>"
    return HttpResponse(html)

def hours_before(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    dt = datetime.now() - timedelta(hours=offset)
    html = f"<html><body><font color='brown'>In {offset} hours ago, it was {dt}.</font></body></html>"
    return HttpResponse(html)
