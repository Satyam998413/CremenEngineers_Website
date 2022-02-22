from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse("shop")
    return render(request,"shop/index.html")

def about(request):
  
    return render(request,"shop/about.html")

def contact(request):
   
    return render(request,"shop/contact.html")

def tracker(request):
   
    return render(request,"shop/tacker.html")

def about(request):
   return render(request,"shop/about.html")

def search(request):
  return render(request,"shop/search.html")

def productView(request):
    return render(request,"shop/productview.html")

def checkout(request):
 return render(request,"shop/checkout.html")