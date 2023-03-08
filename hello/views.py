from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.


def index(request):
    return render(request,'hello/index.html')




def greet(request,name):
    nameso = ['mo3z','niga abdo','tall niger ahmed']
    return render(request, 'hello/name.html',{'name':name,'nameso':nameso})