from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
# Create your views here.

def index(request):
    return render(request,'Home.html')
