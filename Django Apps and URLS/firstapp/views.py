from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home1(request):
    return HttpResponse("Hello World Home 1")

def home2(request):
    return HttpResponse("<b>Hello World Home 2<b>")