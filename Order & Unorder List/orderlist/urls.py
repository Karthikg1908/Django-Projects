from django.urls import path
from . views import fruit_stu
urlpatterns = [
    path('',fruit_stu,name='fruit_stu')
]