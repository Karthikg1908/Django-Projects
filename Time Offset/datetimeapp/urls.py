from django.urls import path 
from . import views
urlpatterns=[
    path('',views.offset_datetime, name='offset_datetime')
]