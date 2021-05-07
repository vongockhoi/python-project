from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'pages/home.html')    
def sanpham(request):
    return render(request, 'pages/sanpham.html')