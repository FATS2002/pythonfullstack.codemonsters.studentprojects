from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def thirdapp_v1(request):
    s='<h1>This is function 1 from thirdapp</h1>'   
    return HttpResponse(s)
def thirdapp_v2(request):
    s='<h1>This is function 2 from thirdapp</h1>'   
    return HttpResponse(s)
def thirdapp_v3(request):
    s='<h1>This is function 3 from thirdapp</h1>'   
    return HttpResponse(s)
