from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    pro1=sampleapp.objects.all 
    return render(request,'index.html',{'pro2':pro1})
