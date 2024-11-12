from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def current_datetime(request):
    now=datetime.datetime.now()
    html=f"""<html>
<head>
    <title>Current Date & Time</title>
</head>
<body style="text-align: center; padding-top: 50px;">
    <div style=" padding: 20px; border: 1px solid #cccccc;">
        <h1>Current Date & Time</h1>
        <p style="font-size: 18px; color: #555555;">{now}</p>
    </div>
</body>
</html>
"""
    return HttpResponse(html)
    