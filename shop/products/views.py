from django.shortcuts import render
from . models import products

# Create your views here.
from django.http import HttpResponse
def index(request):
    pro1=products.objects.all  #table name-products
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,'index.html',{'pro2':pro1}) #3rd parameter, pro2 can access template value.
def about(request):
    return HttpResponse("<h1>This is About Page</h1>")