from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines("<h1>xin chao</h1>")
    response.write("day la apphome")
    return response    