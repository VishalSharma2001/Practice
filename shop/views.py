from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.http import HttpRequest
from shop.models import Product
# Create your views here.
from math import ceil

def index(request):
    products=Product.objects.all()
    
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)+(n//4))
        allProds.append([prod,range(1,nSlides),nSlides]) 



    #print(products)
    #params={"no_of_slides":nSlides,'range':range(1,nSlides),'product':products}
    # allProds=[[products,range(1,nSlides),nSlides],
    #           [products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
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
