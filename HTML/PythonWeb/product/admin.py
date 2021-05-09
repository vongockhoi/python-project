from django.contrib import admin
from .models import NhanHieu,SanPham
# Register your models here.
class NhanHieuAdmin(admin.ModelAdmin):
    list_display = ['TenNH','date']
    list_filter = ['date']
    search_fields = ['TenNH']
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ['TenNH','TenSP','SoLuong','Gia','date']

admin.site.register(NhanHieu, NhanHieuAdmin)
admin.site.register(SanPham, SanPhamAdmin)
