
from django.shortcuts import render   
from django.http import HttpResponse   
   
 # Create your views here.   
def app1_view1(request):
    s='<h1>This is function1 from firstapp</h1>'   
    return HttpResponse(s)
def app1_view2(request):
    s='<h1>This is function2 from firstapp</h1>'   
    return HttpResponse(s)
def app1_view3(request):
    s='<h1>This is function3 from firstapp</h1>'   
    return HttpResponse(s)