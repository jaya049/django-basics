from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    title="Orisys Academy For Skill Development & Research"
    return render(request, 'orisys/home.html', {'title': title})

