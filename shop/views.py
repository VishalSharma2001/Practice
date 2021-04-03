from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("This is About Page")
def contact(request):
    return HttpResponse("This is contact Page")
def tracker(request):
    return HttpResponse("This is tracker Page")
def search(request):
    return HttpResponse("This is search Page")
def productview(request):
    return HttpResponse("This is productview Page")
def checkout(request):
    return HttpResponse("This is checkout Page")
