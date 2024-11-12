from django.shortcuts import render
from django.template import loader

# Create your views here.

def fruit_stu(request):
    fruits=['Apple','Mango','Graphs','Banana','Cherry','Kiwi']
    student=['Karthi','Abhi','Prashanth','Lakshmi','Pranita','Madhrui']
    return render (request,'index.html',{'fruits':fruits,'student':student}) 

    