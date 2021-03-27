from django.shortcuts import render
from . models import Customer
from . models import Product
from . models import Order
#from django.http import HttpResponse
# Create your views here.
def index(request):
    pro1=Customer.objects.all()
    #pro2=Product.objects.all()
    order=Order.objects.all()
    total_order=order.count()
    delivered=order.filter(status='Delivered').count()
    pending=order.filter(status='Pending').count()
    context={'customer':pro1,'order':order,'total_order':total_order,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def product(request):
    product=Product.objects.all()
    return render(request,'accounts/product.html',{'product':product})

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    context={'customer':customer}
    return render(request,'accounts/customer.html',context)
