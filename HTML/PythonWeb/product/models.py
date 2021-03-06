from django.db import models

# Create your models here.
class NhanHieu(models.Model):
    TenNH = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.TenNH}"
class SanPham(models.Model):
    TenNH = models.ForeignKey(NhanHieu, on_delete = models.CASCADE)
    TenSP = models.CharField(max_length=100)
    SoLuong = models.IntegerField(blank=True,null=True)
    Gia = models.FloatField()
    image = models.ImageField(null =True)
    date = models.DateTimeField(auto_now_add=True)