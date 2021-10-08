
from django.contrib.auth import *
from django.db import models
from django.contrib import admin
from django.db.models.fields import BooleanField
from django.db.models.fields.related import OneToOneField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from ckeditor.fields import *
from ckeditor_uploader.fields import *
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.conf import settings
from datetime import date
from django.utils.html import mark_safe

class Phongban(models.Model):
    tenpb = models.CharField(default='',unique=True,max_length=255,verbose_name='Tên Phòng Ban')
    ngaythanhlap = models.DateTimeField(verbose_name='Năm thành lập',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name = "1. PHÒNG BAN"
        verbose_name_plural = '1. PHÒNG BAN'

    def __str__(self):
        return self.tenpb

class Nhanvien(models.Model):
    manv = models.CharField(default='',unique=True,max_length=255,verbose_name='Mã Nhân Viên')
    username = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Tài Khoản Nhân Viên') #OneToOneField
    tennv = models.CharField(default='', max_length=255, verbose_name='Họ Tên Nhân Viên')
    gioitinh = models.BooleanField(default='',verbose_name='Check - Nếu là nam')
    ngaysinh =models.DateField(verbose_name='Ngày Sinh')
    diachi = models.CharField(default='', max_length=255, verbose_name='Địa chỉ thường trú')
    diachihientai = models.CharField(default='', max_length=255, verbose_name='Địa chỉ Hiện Tại')
    sos = models.IntegerField(default=0,null=True,blank=True,verbose_name="Số Điện Thoại Khẩn Cấp")
    quequan =models.CharField(default='', max_length=255, verbose_name='Quê Quán')
    masohs = models.CharField(default='',blank=True,null=True,max_length=255,verbose_name='Mã Số HDLD ')
    ngaythuviec =  models.DateField(blank=True,null=True,verbose_name='Ngày thử việc')
    ngaychinhthuc = models.DateField(blank=True,null=True,verbose_name='Ngày làm chính thức')
    chuyenmon = models.CharField(default='',blank=True,null=True,max_length=255, verbose_name='Chuyên ngành')
    vanhoa = models.CharField(default='',blank=True,null=True, max_length=255, verbose_name='Trình độ')
    cmnd = models.CharField(default='', max_length=12, verbose_name='CMND/CCID')
    cmnd_1 =models.ImageField(default='',upload_to='img/', verbose_name='Ảnh mặt trước CMND/CCID')
    cmnd_2 =models.ImageField(default='',null=True, blank=True, upload_to='img/', verbose_name='Ảnh mặt sau CMND/CCID')
    ngaycap =  models.DateField(blank=True,null=True,verbose_name='Ngày Cấp')
    noicap = models.CharField(default='',null=True, blank=True, max_length=255, verbose_name='Nơi Cấp ')
    avatar = models.ImageField(default='',upload_to='img/', verbose_name='Ảnh chân dung')
    sdt = models.CharField(default='', unique=True, blank=True,null=True,max_length=255, verbose_name='Số Điện Thoại Công Ty ')
    sdt2 = models.CharField(default='',blank=True,null=True,max_length=255, verbose_name='Số Điện Thoại Cá Nhân')
    line= models.CharField(default='', blank=True,null=True,max_length=255, verbose_name='Line nội bộ')
    email =models.CharField(default='',unique=True, null=True,blank=True ,max_length=255, verbose_name='Email')
    phongban = models.ForeignKey(Phongban,default='',null=True,blank=True,on_delete=models.CASCADE)
    vitricongviec = models.CharField(default="",null=True,blank=True,max_length=255,verbose_name="Vị Trí Công Việc") 
    tinhtrangcongviec = models.BooleanField(default='1',verbose_name='Check --- (nếu nhân viên chính thức) ')
    thoiviec = models.BooleanField(default=False,verbose_name='Check --- (nếu nhân viên đã Nghỉ Việc ) ')
    ngaythoiviec =  models.DateField(blank=True,null=True,verbose_name='Ngày Nghỉ Việc ')
    lydonghiviec = models.CharField(default="" ,max_length=1000,blank=True,null=True)
    chuky1 =models.FileField(blank=True,null=True,verbose_name='Upload chữ ký 1 ')
    chuky2 = models.FileField(blank=True, null=True, verbose_name='Upload chữ ký 2 ')
    qr_code = models.ImageField(upload_to='qr_codes/nhanvien/', blank=True,verbose_name="QR CODE - (Không thêm mới hoặc chỉnh sửa ")
    tinhtranghonnhan = models.CharField(max_length=255,null=True,blank=True,choices=[('Độc Thân',"Độc Thân"),('Đã Kết Hôn',"Đã Kết Hôn")],verbose_name="Tình Trạng Hôn Nhân ")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering =['id']
        verbose_name = "2. NHÂN VIÊN"
        verbose_name_plural = '2. NHÂN VIÊN'
        

    def __str__(self):
        return self.tennv
    @property
    def avatar_preview(self):
        if self.avatar:
            return mark_safe('<img src="{}" width="220" height="180" />'.format(self.avatar.url))
        return ""
    @property
    def cmnd_1_preview(self):
        if self.cmnd_1:
            return mark_safe('<img src="{}" width="220" height="180" />'.format(self.cmnd_1.url))
        return ""

    def save(self, *args, **kwargs):
       
        qrcode_img = qrcode.make('http://dongsapa.net/ed5511ad61be3b785518eddc96e4bc3f11ad61be3b785518eddc96e4bc3f11ad61be3b785518eddc96e4bc3f11ad61be3b785518eddc96e4bc3f11ad61be3b785518eddc96e4bc3f-ed5511ad61be3b785518eddc96e4bc3f'+str(self.id))
        canvas = Image.new('RGB', (760,680), 'white')
        canvas.paste(qrcode_img)
        fname = f'ma-qr-code-{self.manv}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Luutamnhanvien(models.Model):
    nhanvien = models.OneToOneField(Nhanvien ,on_delete=models.CASCADE,verbose_name='Nhân Viên')
    sdtcn = models.CharField(default=" " ,max_length=20,blank=True,verbose_name="Điện Thoại Cá Nhân" )
    dcht = models.CharField(default=" " ,max_length=255,null=True,blank=True,verbose_name="Địa chỉ hiện tại" )
    cmnd = models.CharField(default=" " ,max_length=255,null=True,blank=True,verbose_name="Chứng Minh Nhân Dân")
    file_cmnd_1 = models.FileField(upload_to="nhanvien/hosonhanvien/luutam" ,null=True,blank=True,verbose_name="Mặt Trước Chứng Minh Nhân Dân")
    file_cmnd_2 = models.FileField(upload_to="nhanvien/hosonhanvien/luutam" ,null=True,blank=True,verbose_name="Mặt Sau Chứng Minh Nhân Dân")
    ngaycap = models.DateField(default=" " ,max_length=20,null=True,blank=True,verbose_name="Ngày Cấp Chứng Minh Nhân Dân")
    noicap = models.CharField(default=" " ,max_length=20,null=True,blank=True,verbose_name=" Nới Cấp Chứng Minh Nhân Dân")
    duyet= models.BooleanField()
    huy = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['-id']
        verbose_name = "DUYỆT CẬP NHẬT HỒ SƠ "
        verbose_name_plural = 'DUYỆT CẬP NHẬT HỒ SƠ '

class Tiemvecxincovid(models.Model):
    nhanvien = models.OneToOneField(Nhanvien ,on_delete=models.CASCADE,verbose_name='Nhân Viên')
    qrcode_vecxin = models.FileField(upload_to="nhanvien/qr_vecxin",verbose_name="Mã Qr Code Chứng Nhận Tiêm Vecxin")
    muitiem = models.IntegerField(default=0,verbose_name="Số Mũi Đã Tiêm")
    ngaytiemgannhat = models.DateField(verbose_name="Ngày Tiêm Gần Nhất ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['id']
        verbose_name = "TIÊM VẮC  XIN COVID "
        verbose_name_plural = 'TIÊM VẮC XIN COVID '


class Chucvu_Congviec(models.Model):

    nhanvien = models.OneToOneField(Nhanvien ,unique=True ,on_delete=models.CASCADE,verbose_name='Nhân Viên')
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name='Phòng ban')
    tencongviec = models.CharField(default='', max_length=255, verbose_name='Tên Công việc+ Chúc Vụ')
    motacongviec = models.TextField(verbose_name='Mô tả công việc')
    
    class Meta:
        verbose_name = "NHÂN VIÊN CHỨC VỤ"
        verbose_name_plural = "NHÂN VIÊN CHỨC VỤ"

    def __int__(self):
        return self.nhanvien

class Baohiemyte(models.Model):
    nhanvien =models.OneToOneField(Nhanvien, on_delete=models.CASCADE)
    masobhyt = models.CharField(default='', unique=True, max_length=255, verbose_name='Mã Số BHXH')
    ngaythamgia = models.DateField(verbose_name='Ngày tham gia')
    noidangky = models.CharField(default='', max_length=255, verbose_name='Nơi đăng ký BHYT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['id']
        verbose_name = "4. BẢO HIỂM Y TẾ"
        verbose_name_plural = '4. BẢO HIỂM Y TẾ'
    def __str__(self):
        return self.masobhyt

class Baohiemxahoi(models.Model):
    nhanvien = models.OneToOneField(Nhanvien, on_delete=models.CASCADE)
    masobhxh = models.CharField(unique=True,max_length=255,verbose_name='Mã Số BHXH')
    ngaythamgia =  models.DateField(verbose_name='Ngày tham gia')
    
    noidangky = models.CharField(max_length=255,null=True,blank=True, choices=[('BHXH Hóc Môn','BHXH Hóc Môn'),('BHXH Quận 3','BHXH Quận 3')], verbose_name='Địa chỉ đăng ký')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering =['id']
        verbose_name = "3. BẢO HIỂM XÃ HỘI"
        verbose_name_plural = '3. BẢO HIỂM XÃ HỘI'
    def __str__(self):
        return self.masobhxh


class Loaihopdong(models.Model):
    maloaihd = models.CharField(default='', max_length=255, verbose_name='Tên Hợp Đồng')
    tenhd = models.CharField(default='', max_length=255,blank=True,null=True, verbose_name='Mô Tả Hợp Đồng')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "LOẠI HỢP ĐỒNG"
        verbose_name_plural = 'LOẠI HỢP ĐỒNG'

    def __str__(self):
        return self.maloaihd

class Quanlyhopdongkinhdoanh(models.Model):
    masohopdong = models.CharField(default='',unique=True, max_length=255, verbose_name='Mã Số Hợp Đồng')
    tenhopdong  = models.CharField(default='', max_length=255, verbose_name='Tên Hợp Đồng')
    khachhang = models.CharField(default='', max_length=255, verbose_name='Tên Khách Hàng')
    ngaytrinhky = models.DateField(default='', max_length=255, verbose_name='Ngày Trình Ký Hợp Đồng')
    filehopdong = models.FileField()
    loaihd  = models.ForeignKey(Loaihopdong,default='',on_delete=models.CASCADE, verbose_name='Loại Hợp Đồng')
    nhanvien = models.ForeignKey(Nhanvien,default='',on_delete=models.CASCADE, verbose_name='Nhân Viên phụ trách')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "QUẢN LÝ HỢP ĐỒNG CÔNG TY"
        verbose_name_plural = 'QUẢN LÝ HỢP ĐỒNG CÔNG TY'

    def __int__(self):
        return self.nhanvien


class Phieuluong_upload(models.Model):
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    thang = models.CharField(default='',null=True, blank=True, max_length=255)
    nam = models.CharField(default='',null=True, blank=True, max_length=255)
    ngaylamthucte = models.CharField(default='', null=True, blank=True,max_length=255)
    congchuan = models.CharField(default='', null=True, blank=True,max_length=255)
    congthembot = models.CharField(default='',null=True, blank=True, max_length=255)
    luongcoban = models.CharField(default='',null=True, blank=True, max_length=255)
    phucap = models.CharField(default='',null=True, blank=True, max_length=255)
    tiendienthoai = models.CharField(default='', null=True, blank=True,max_length=255)
    tienxang = models.CharField(default='', null=True, blank=True,max_length=255)
    tiencom = models.CharField(default='',null=True, blank=True, max_length=255)
    luongtrachnhiem = models.CharField(default='',null=True, blank=True, max_length=255)
    tiendienthoaihotro = models.CharField(default='',null=True, blank=True, max_length=255)
    ngaynghikhongpep = models.CharField(default='',null=True, blank=True, max_length=255)
    truluongnghikhongphep = models.CharField(default='', null=True, blank=True,max_length=255)
    hotrobaohiemtrongluong = models.CharField(default='', null=True, blank=True,max_length=255)
    luoncnx2 = models.CharField(default='', null=True, blank=True,max_length=255)
    tongthunhap = models.CharField(default='', null=True, blank=True,max_length=255)
    trutienunggiuathang = models.CharField(default='',null=True, blank=True, max_length=255)
    trutienmatunggiuathang = models.CharField(default='', null=True, blank=True,max_length=255)
    trutiendienthoaicongtytraho = models.CharField(default='',null=True, blank=True, max_length=255)
    trunotrongthang = models.CharField(default='',null=True, blank=True, max_length=255)
    trubaohiem = models.CharField(default='', null=True, blank=True,max_length=255)
    trutienphat = models.CharField(default='',null=True, blank=True, max_length=255)
    truluongluyke = models.CharField(default='', null=True, blank=True,max_length=255)
    tienluongthuclanhcuoithang = models.CharField(default='',null=True, blank=True, max_length=255)
    nothangtruoc = models.CharField(default='', null=True, blank=True,max_length=255)
    muonnothangnay = models.CharField(default='', null=True, blank=True,max_length=255)
    trunotrongluong = models.CharField(default='',null=True, blank=True, max_length=255)
    thunotienmat = models.CharField(default='', null=True, blank=True, max_length=255)
    noconluanchuyensangthangsau = models.CharField(default='',null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = " UPLOAD PHIẾU LƯƠNG"
        verbose_name_plural = 'UPLOAD PHIẾU LƯƠNG'

    def __int__(self):
        return self.nhanvien


class Dexuat(models.Model):  
    
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    tieude = models.CharField(max_length=500,default="",null=False)
    noidung = RichTextUploadingField()
    files = models.FileField(blank=True,null=True,upload_to='filedexuat/')
    guiduyet= models.CharField(max_length=20, choices=[('0','Gửi Sếp'),('1',' Chỉ Gửi Trưởng Phòng')], verbose_name='Trạng Thái Gửi Duyệt')
    hangmuc = models.CharField(max_length=20, choices=[('0','Hàng Hóa'),('1','Mua Sắm Thiết Bị'),('2','Khác')], verbose_name='Hạng Mục')
    trangthaiduyet_tp = models.BooleanField()
    trangthaiduyet_sep = models.BooleanField()
    tinhtrangxem = models.BooleanField()
    tinhtranghuy = models.BooleanField()
    kinhphi = models.IntegerField(default=0)
    tinhtrangtamung = models.BooleanField()
    tientamung = models.IntegerField(default=0)
    tinhtranggiaichi = models.BooleanField(default=False)
    ghichu = models.TextField(default="",max_length=255,blank=True,null=True)
    nhanviencc = models.JSONField( max_length=1000,blank=True,null = True)
    thoigianhoanthanh = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    class Meta:

        verbose_name = "FORM ĐỀ XUẤT"
        verbose_name_plural = 'ĐỀ XUẤT'

    def __int__(self):
        return self.nhanvien


class Giaichi(models.Model):
    dexuat = models.ForeignKey(Dexuat,on_delete=models.CASCADE,blank=True,null=True)
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE)
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    guiduyet= models.CharField(max_length=20, choices=[('0','Gửi Sếp'),('1',' Chỉ Gửi Trưởng Phòng'),('2',' Tài Chính Kế Toán')], verbose_name='Trạng Thái Gửi Duyệt')
    hangmuc = models.CharField(max_length=20, choices=[('0','Hàng Hóa'),('1','Mua Sắm Thiết Bị'),('2','Khác')], verbose_name='Hạng Mục')
    noidungdexuat =  RichTextUploadingField(null=True,blank=True)
    giaichikhac   =   RichTextUploadingField(null=True,blank=True)
    giaichihanghoa = RichTextUploadingField(blank=True,null = True,verbose_name='Hàng Hóa')
    giaichithietbi = models.JSONField(blank=True,null = True,verbose_name='Trang Thiết Bị')
    tieude = models.CharField(default="",max_length=500,null=False)
    ghichu = models.CharField(default="Thu Quy :",max_length=500,null=False)
    
    trangthaiduyetgiaichi = models.BooleanField()
    trangthaiduyet_tp = models.BooleanField()
    trangthaiduyet_tckt = models.BooleanField()
    trangthaiduyet_sep = models.BooleanField()
    trangthaihuy = models.BooleanField()
    trangthaihoanthanh = models.BooleanField()
    noidungthanhtoan =  RichTextUploadingField(null=True,blank=True)
    tientamung  = models.IntegerField(default=0)
    tiengiaichi = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:

        verbose_name = "GIAI CHI "
        verbose_name_plural = 'GIAI CHI'

    def __int__(self):
        return self.nhanvien
class Filegiaichis(models.Model):
    giaichi=models.ForeignKey(Giaichi,on_delete=models.CASCADE)
    files = models.FileField(null=True,blank=True,default="",upload_to="giaichi/") 
    
    class Meta:
        verbose_name = "FILE GIAI CHI"
        verbose_name_plural = "FILE GIAI CHI"
    def __int__(self):
        return self.giaichi
    
class Motacongviec(models.Model):
    tieude = models.CharField(default="",max_length=255,verbose_name="Tiêu Đề Công Việc")
    file = models.FileField(default="",null=True,blank=True,upload_to='motacongviec/',verbose_name="Upload file (có thể đẻ trông)")
    motacongviec = RichTextUploadingField(verbose_name = "Nội Dung Công Việc")
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name="Phòng Ban")
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name="Nhân Viên Áp Dụng")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "5. MÔ TẢ CÔNG VIỆC"
        verbose_name_plural = '5. MÔ TẢ CÔNG VIỆC'

    def __int__(self):
        return self.nhanvien

  
class Kienthucnen(models.Model):
    tieude = models.CharField(default="",max_length=255,verbose_name="Tiêu Đề Công Việc")
    noidung = RichTextUploadingField(verbose_name = "Nội Dung Công Việc")
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name="Phòng Ban Áp Dụng")
    tacgia = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name="Tác Giả Bài Viết")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "6. KIẾN THỨC NÉN CHO NHÂN VIÊN "
        verbose_name_plural = '6. KIẾN THỨC NÉN CHO NHÂN VIÊN '

    def __int__(self):
        return self.tieude


class Cauhoithuonggap(models.Model):
    cauhoi = models.CharField(default="",max_length=255,verbose_name="Tên Câu Hỏi Thường Gặp")
    traloi = RichTextUploadingField(verbose_name = "Nội Dung Trả lời")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "7. CÂU HỎI THƯỜNG GẶP"
        verbose_name_plural = '7. CÂU HỎI THƯỜNG GẶP'

    def __int__(self):
        return self.cauhoi


class Hoidap(models.Model):
    cauhoi = models.CharField(default="",max_length=255,verbose_name="Câu Hỏi của Nhân Viên")
    idnhanvienhoi = models.IntegerField() 
    nhanvienhoi = models.CharField(default="",max_length=255, verbose_name="Nhân Viên Đặt câu hỏi")
    phongbantraloi = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name="Phòng Ban Phải Trả Lời")
    traloi = RichTextUploadingField(blank =True,null=True,verbose_name = "Nội Dung trả lời")
    nhanvientraloi = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,blank =True,null=True,verbose_name="Nhân Viên Trả Lời")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "8. HỎI ĐÁP NHÂN VIÊN"
        verbose_name_plural = '8. HỎI ĐÁP NHÂN VIÊN'

    def __int__(self):
        return self.cauhoi

class Xinphep(models.Model):
    nhanvien = models.ForeignKey(Nhanvien,on_delete=models.CASCADE,verbose_name="Nhân Viên ")
    ngaynghi = models.DateField(default = date.today,verbose_name="Ngày Nghỉ Phép")
    ngaylamlai = models.DateField(verbose_name="Ngày đi làm lại ")
    phongban = models.ForeignKey(Phongban,on_delete=models.CASCADE,verbose_name="Phòng Ban",null=True,blank=True)
    lydo = models.CharField(default="" ,max_length=1000,verbose_name="Lý Do Xin Nghỉ")
    lienlac = models.CharField(default="" ,max_length=1000,null=True,blank=True,verbose_name="Liên Lạc Khẩn Cấp ")
    
    guiduyet= models.CharField(max_length=20, choices=[('1','Gửi Sếp'),('2',' Chỉ Gửi Trưởng Phòng')], verbose_name=' Gửi Duyệt')
    sep_duyet = models.BooleanField(default=False)
    tp_duyet = models.BooleanField(default=False)
    huy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = " XIN NGHỈ PHÉP "
        verbose_name_plural = ' XIN NGHỈ PHÉP'

    def __int__(self):
        return self.nhanvien