from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse   
    
# Create your views here.   
def display(request):
    s='<h1>Changing the port number</h1>'   
    return HttpResponse(s)   
