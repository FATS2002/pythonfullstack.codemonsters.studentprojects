from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def secondapp_v1(request):
    s='<h1>This is function 1 from secondapp</h1>'   
    return HttpResponse(s)
def secondapp_v2(request):
    s='<h1>This is function 2 from secondapp</h1>'   
    return HttpResponse(s)
def secondapp_v3(request):
    s='<h1>This is function 3 from secondapp</h1>'   
    return HttpResponse(s)
