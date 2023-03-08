from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'hello/index.html')




def greet(request,name):
    nameso = {'name1': 'moaz','name2':'ahmed','name3':'abdo'}
    return render(request, 'hello/name.html',{'nameso':nameso,'name':name})