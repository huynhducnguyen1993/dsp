from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from qlns.models import Nhanvien
from qlns.resources import NhanvienResource
from datetime import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .forms import *
# Register your models here.
from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile
from django.db.models.functions import Lower

admin.site.site_header="Đông Sapa"


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        

class UserAdmin(ExportMixin, UserAdmin):
    resource_class = UserResource
    

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class PhieuluongAdmins(ImportExportActionModelAdmin):
    list_display = ('id','nhanvien', 'thang', 'nam', 'tongthunhap')
    search_fields = ('nhanvien',)
    list_filter = ('thang','nam')
    list_per_page = 10
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)


admin.site.register(Phieuluong_upload, PhieuluongAdmins)

class VecxinAdmins(admin.ModelAdmin):
    list_display = ('id','nhanvien', 'muitiem', 'ngaytiemgannhat', )
    search_fields = ('nhanvien',)
    list_filter = ('nhanvien',)
    list_per_page = 10
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)


admin.site.register(Tiemvecxincovid,VecxinAdmins)

admin.site.register(Loaihopdong)



class AdminThumbnailSpec(ImageSpec):
    processors = [ResizeToFill(220, 180)]
    format = 'JPEG'
    options = {'quality': 60 }

def cached_admin_thumb(instance):
    # `image` is the name of the image field on the model
    cached = ImageCacheFile(AdminThumbnailSpec(instance.qr_code))
    # only generates the first time, subsequent calls use cache
    cached.generate()
    return cached

class NhanvienAdmins(ImportExportActionModelAdmin):
    
    list_display = ('__str__','id','manv', 'tennv', 'username', 'admin_qrcode','avatar_preview','cmnd_1_preview',)
    search_fields = ('tennv',)
    list_filter = ('phongban',)
    
    readonly_fields =('avatar_preview',)
    list_per_page = 20
    resource_class = NhanvienResource
    form = AddnhanvienAdmin
    fieldsets= (('Thông Tin Nhân Viên ',{
                            'fields':('manv','username','tennv','gioitinh','ngaysinh','diachi','diachihientai','quequan',),
                             
                       }),
                   ('Hồ Sơ  Nhân Viên ',{
                            'fields':('phongban','vitricongviec','tinhtrangcongviec','masohs','ngaythuviec','ngaychinhthuc','chuyenmon','vanhoa',),
                             
        }),
                     ('Chứng Minh Nhân Dân - Thẻ Căn Cước  ',{
                            'fields':('cmnd','cmnd_1','cmnd_2','ngaycap','noicap',),
                             
        }),
                     ('Liên Hệ   ',{
                            'fields':('sdt','sdt2','line','email',),
                             
        }),
                ('Chân Dung - Chử Ký -QR Code  ',{
                            'fields':('avatar','chuky1','chuky2','qr_code',),
                             
        }),
        
                ('Nhân Viên Thôi Việc   ',{
                            'fields':('thoiviec','ngaythoiviec','lydonghiviec',),
                             
        }),
         ('Hôn Nhân    ',{
                            'fields':('tinhtranghonnhan','sos',),
                             
        }),
        )
    admin_qrcode = AdminThumbnail(image_field=cached_admin_thumb)
    admin_qrcode.short_description = "QR Nhân Viên "
    def avatar_preview(self, obj):
        return obj.avatar_preview

    avatar_preview.short_description = 'Chân Dung'
    avatar_preview.allow_tags = True

    def cmnd_1_preview(self, obj):
        return obj.cmnd_1_preview

    cmnd_1_preview.short_description = 'CMND/CCID Mặt Trước'
    cmnd_1_preview.allow_tags = True
    def cmnd_2_image(self, obj):
        if obj.cmnd_2.url:
            url = obj.cmnd_2.url,
            width=obj.cmnd_2.width,
            height=obj.cmnd_2.height,
            

        else:
            url = obj.cmnd_1.url,
            width = 0,
            height = 0,
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url,width,height))

admin.site.register(Nhanvien, NhanvienAdmins)

class PhongbanAdmin(ImportExportActionModelAdmin):
    list_display = ('id','tenpb', 'ngaythanhlap','view_nhanvien')
    import_id_fields = ('code',)
    skip_unchanged = True
    report_skipped = True
    def view_nhanvien(self,obj):
        count = obj.nhanvien_set.count()
        url = (
                reverse("admin:qlns_nhanvien_changelist")
                + "?"
                + urlencode({"phongban__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} nhân Viên</a>', url, count)

    view_nhanvien.short_description = "Số Nhân Viên"
    # tính tổng nhân viên trong 1 phòngs

    def before_save_instance(self, instance):
        format_str = '%d/%m/%y'  # the format in which dates are stored in CSV file
        instance.created_at = datetime.strptime(instance.created_at, format_str)
        instance.updated_at = datetime.strptime(instance.updated_at, format_str)
        return instance



admin.site.register(Phongban, PhongbanAdmin)


# class NhanvienAdmin(admin.ModelAdmin):
#     list_display = ('manv', 'tennv', 'username', 'cmnd_1')
#     list_filter = ('phongban',)
#     search_fields = ('tennv',)
#     list_per_page = 10
#
# admin.site.register(Nhanvien, NhanvienAdmin)




class NhanvienChucvuAdmin(admin.ModelAdmin):
    list_display = ('nhanvien', 'phongban','tencongviec')
    list_filter =('phongban',)


admin.site.register(Chucvu_Congviec, NhanvienChucvuAdmin)

class BaohiemxahoiAdmin(admin.ModelAdmin):
    list_display = ('nhanvien', 'masobhxh','ngaythamgia','noidangky')
    list_filter = ('nhanvien__phongban',)

admin.site.register(Baohiemxahoi, BaohiemxahoiAdmin)



class XinphepAdmins(admin.ModelAdmin):
    list_display = ('nhanvien', 'ngaynghi','ngaylamlai')
    list_filter = ('nhanvien__phongban',)

admin.site.register(Xinphep, XinphepAdmins)


class BaohiemytAdmin(admin.ModelAdmin):
    list_display = ('nhanvien', 'masobhyt','ngaythamgia','noidangky')
    list_filter = ('nhanvien__phongban',)

admin.site.register(Baohiemyte, BaohiemytAdmin)

# class HosoAdmin(admin.ModelAdmin):
#     list_display = ('nhanvien', 'masobh','ngaythuviec','ngaychinhthuc')


# admin.site.register(Hosonhanvien, HosoAdmin)

class HosokinhdoanhAdmin(admin.ModelAdmin):
    list_display = ('masohopdong', 'tenhopdong','ngaytrinhky','filehopdong','nhanvien','created_at','updated_at')
    list_filter = ('nhanvien__phongban',)

admin.site.register(Quanlyhopdongkinhdoanh, HosokinhdoanhAdmin)

class DexuatAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanvien','phongban','tieude','files')
    list_filter = ('phongban',)
    search_fields = ('nhanvien',)
    list_per_page = 10
    import_id_fields = ('id',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)

admin.site.register(Dexuat, DexuatAdmin)

class GiaichiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanvien','phongban','tieude')
    list_filter = ('phongban',)
    search_fields = ('nhanvien',)
    list_per_page = 10
    import_id_fields = ('id',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    readonly_fields = ("created_at",)
    def before_save_instance(self, instance):
        format_str = '%d/%m/%y'  # the format in which dates are stored in CSV file
        instance.created_at = datetime.strptime(instance.created_at, format_str)
        instance.updated_at = datetime.strptime(instance.updated_at, format_str)
        return instance

admin.site.register(Giaichi, GiaichiAdmin)



class MotacongviecAdmin(admin.ModelAdmin):
    list_display = ('id', 'nhanvien','phongban','tieude')
    list_filter = ('phongban',)
    search_fields = ('nhanvien',)
    list_per_page = 10
    import_id_fields = ('id',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    


admin.site.register(Motacongviec, MotacongviecAdmin)



class kienthucnenAdmin(admin.ModelAdmin):
    list_display = ('id', 'tieude','phongban',)
    list_filter = ('phongban',)
    search_fields = ('tieude',)
    list_per_page = 10
    import_id_fields = ('id',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    


admin.site.register(Kienthucnen, kienthucnenAdmin)


class CauhoithuonggapAdmin(admin.ModelAdmin):
    list_display = ('id', 'cauhoi','created_at',)
    list_filter = ('created_at',)
    search_fields = ('cauhoi',)
    list_per_page = 10
    import_id_fields = ('id',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    


admin.site.register(Cauhoithuonggap, CauhoithuonggapAdmin)

class HoidapAdmin(admin.ModelAdmin):
    list_display = ('id', 'cauhoi','nhanvienhoi','phongbantraloi','nhanvientraloi','created_at',)
    list_filter = ('created_at',)
    search_fields = ('cauhoi',)
    list_per_page = 10
    import_id_fields = ('id',)
    skip_unchanged = True
    report_skipped = True
    exclude = ('id',)
    


admin.site.register(Hoidap, HoidapAdmin)
