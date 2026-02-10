from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstapp_v1(request):
    s='<h1>This is function 1 from firstapp</h1>'   
    return HttpResponse(s)
def firstapp_v2(request):
    s='<h1>This is function 2 from firstapp</h1>'   
    return HttpResponse(s)
def firstapp_v3(request):
    s='<h1>This is function 3 from firstapp</h1>'   
    return HttpResponse(s)