from django.shortcuts import render
from django . http import HttpResponse 
from datetime import datetime,timedelta

# Create your views here.

from datetime import datetime, timedelta
from django.http import HttpResponse

from datetime import datetime, timedelta
from django.http import HttpResponse

def offset_datetime(request):
    current_datetime = datetime.now()
    offset_hours = 4
    offset_before = current_datetime - timedelta(hours=offset_hours)
    offset_after = current_datetime + timedelta(hours=offset_hours)
    html = f"""
    <html>
    <head>
    <title>Offset Date & Time</title>
    </head>
    <body style="text-align: center; padding-top: 50px;">
        <div style="padding: 20px; border: 1px solid #cccccc; display: inline-block;">
            <h1>Current Date and Time with Offsets:</h1>
            <p>Current: {current_datetime}</p>
            <p>Four Hours Ahead: {offset_after}</p>
            <p>Four Hours Before: {offset_before}</p>
        </div>
    </body>
    </html>"""
    return HttpResponse(html)

