from django.shortcuts import render
from django.http import HttpResponse   


# Create your views here.
def app2_view1(request):
    s='<h1>This is function1 from secondapp</h1>'   
    return HttpResponse(s)
def app2_view2(request):
    s='<h1>This is function2 from secondapp</h1>'   
    return HttpResponse(s)
def app2_view3(request):
    s='<h1>This is function3 from secondapp</h1>'   
    return HttpResponse(s)