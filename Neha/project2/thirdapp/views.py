from django.shortcuts import render
from django.http import HttpResponse   

# Create your views here.
def app3_view1(request):
    s='<h1>This is function1 from thirdapp</h1>'   
    return HttpResponse(s)
def app3_view2(request):
    s='<h1>This is function2 from thirdapp</h1>'   
    return HttpResponse(s)
def app3_view3(request):
    s='<h1>This is function3 from thirdapp</h1>'   
    return HttpResponse(s)