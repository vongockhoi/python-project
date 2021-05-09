from django.shortcuts import render
from .models import SanPham
# Create your views here.
def list(request):
    Data = {'SanPhams': SanPham.objects.all().order_by("-date")}
    return render(request, 'product/sanpham.html', Data)