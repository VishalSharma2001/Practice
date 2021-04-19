from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
from shop.models import Product
# Create your views here.
from math import ceil

def index(request):
    products=Product.objects.all()
    n=len(products)
    nSlides=n//4+ceil((n/4)+(n//4))
    params={"no_of_slides":nSlides,'range':range(1,nSlides),'product':products}
    return render(request,'index.html',params)
def about(request):
    return render(request,'about.html')
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
