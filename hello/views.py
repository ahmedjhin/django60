from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


def index(request,name):
    return render(request,'hello/index.html',{'name':name})




def greet(request,name):
    return render(request, 'hello/name.html',{'name':name})