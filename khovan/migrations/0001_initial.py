# Generated by Django 3.2.3 on 2021-09-17 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('qlns', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Congsuat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tencongsuat', models.CharField(default='', max_length=100, verbose_name=' Công suất ')),
                ('mota', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả (có thể bỏ trống)')),
            ],
            options={
                'verbose_name': 'CÔNG SUẤT ',
                'verbose_name_plural': 'CÔNG SUẤT ',
            },
        ),
        migrations.CreateModel(
            name='Gas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tengas', models.CharField(default='', max_length=100, verbose_name='Loại Gas')),
                ('mota', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả (có thể bỏ trống)')),
            ],
            options={
                'verbose_name': 'LOẠI GAS',
                'verbose_name_plural': 'LOẠI GAS',
            },
        ),
        migrations.CreateModel(
            name='Hanghoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=0, unique=True)),
                ('tenhanghoa', models.CharField(default='', max_length=100, verbose_name='Tên Hàng Hoá (Dàn Lạnh/ Dàn Nóng.)')),
                ('giavon', models.IntegerField(blank=True, default='0', null=True, verbose_name='Giá Vốn ')),
                ('mota', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả (có thể bỏ trống)')),
                ('congsuat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.congsuat', verbose_name='Công Suất')),
                ('gas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.gas', verbose_name='Loại Gas ')),
            ],
            options={
                'verbose_name': 'HÀNG HOÁ ',
                'verbose_name_plural': 'HÀNG HOÁ',
            },
        ),
        migrations.CreateModel(
            name='Hangsx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenhangsx', models.CharField(default='', max_length=100, verbose_name='Tên Hãng ')),
                ('mota', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả (có thể bỏ trống)')),
            ],
            options={
                'verbose_name': 'HÃNG SX ',
                'verbose_name_plural': 'HÃNG SX ',
            },
        ),
        migrations.CreateModel(
            name='Hemay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenhemay', models.CharField(default='', max_length=100, verbose_name=' Hệ Máy ')),
                ('mota', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả (có thể bỏ trống)')),
            ],
            options={
                'verbose_name': 'HỆ MÁY',
                'verbose_name_plural': 'HỆ MÁY',
            },
        ),
        migrations.CreateModel(
            name='Khohang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenkho', models.CharField(max_length=200, verbose_name='Tên Kho')),
                ('diachi', models.CharField(blank=True, max_length=500, null=True, verbose_name='Địa Chỉ')),
            ],
            options={
                'verbose_name': 'KHO HÀNG ',
                'verbose_name_plural': 'KHO HÀNG',
            },
        ),
        migrations.CreateModel(
            name='Loaimay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenloai', models.CharField(default='', max_length=100, verbose_name='Loại Máy')),
                ('mota', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả (có thể bỏ trống)')),
            ],
            options={
                'verbose_name': 'LOẠI MÁY ',
                'verbose_name_plural': 'LOẠI MÁY ',
            },
        ),
        migrations.CreateModel(
            name='Nganhhang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tennghanhhang', models.CharField(default='', max_length=100, verbose_name='Tên Nghành Hàng ')),
                ('mota', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mô tả (có thể bỏ trống)')),
            ],
            options={
                'verbose_name': 'NGÀNH HÀNG ',
                'verbose_name_plural': 'NGÀNH HÀNG ',
            },
        ),
        migrations.CreateModel(
            name='Nhacungcap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tennhacungcap', models.CharField(max_length=200, verbose_name='Tên Nhà Cung Cấp')),
                ('diachinhacungcap', models.CharField(max_length=200, verbose_name='Địa chỉ nhà cung cấp')),
                ('diachikhonhacungcap', models.CharField(max_length=200, verbose_name='Địa chỉ nhà cung cấp')),
                ('hanmuccongno', models.FloatField(blank=True, default=0, null=True, verbose_name='Hạn mức ')),
                ('nhanvienquanly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlns.nhanvien', verbose_name='Tên Nhân Viên Quản Lý')),
            ],
            options={
                'verbose_name': 'NHÀ CUNG CẤP ',
                'verbose_name_plural': 'NHÀ CUNG CẤP',
            },
        ),
        migrations.CreateModel(
            name='Xuathang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluong', models.IntegerField(default=0, verbose_name='Số Lượng')),
                ('tinhtrang', models.BooleanField(verbose_name='Tình Trạng -(Check Nếu Hàng Đã Thực Xuất)')),
                ('hanghoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.hanghoa', verbose_name='Tên Hàng Hoá')),
                ('kho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.khohang', verbose_name='Tên Kho')),
            ],
            options={
                'verbose_name': 'XUẤT HÀNG ',
                'verbose_name_plural': 'XUẤT HÀNG',
            },
        ),
        migrations.CreateModel(
            name='Ton_kho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluongnhap', models.IntegerField(default=0, verbose_name='Số Lượng Nhập')),
                ('soluongxuat', models.IntegerField(default=0, verbose_name='Số Lượng Xuất')),
                ('hanghoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.hanghoa', verbose_name='Tên Hàng Hoá')),
                ('kho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.khohang', verbose_name='Tên Kho')),
            ],
            options={
                'verbose_name': 'TỒN KHO ',
                'verbose_name_plural': 'TỒN KHO',
            },
        ),
        migrations.CreateModel(
            name='Thukho_Khohang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.khohang')),
                ('nhanvien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qlns.nhanvien')),
            ],
            options={
                'verbose_name': 'THỦ KHO',
                'verbose_name_plural': 'THỦ KHO',
            },
        ),
        migrations.CreateModel(
            name='Phieunhaphang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, unique=True, verbose_name='Barcode')),
                ('noidung', models.JSONField(verbose_name='Nội Dung ')),
                ('nhanvien', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên Kinh doanh(không  điền trường này)')),
                ('guiduyet', models.CharField(choices=[('1', 'Gui Ke Toan'), ('0', 'Khong can gui duyet')], max_length=20, verbose_name='Trang Thai Duyệt')),
                ('tinhtrang', models.BooleanField(verbose_name='Trang Thai Duyệt')),
                ('tuchoi', models.BooleanField(verbose_name='Từ Chối')),
                ('xulykho', models.BooleanField(verbose_name='Xu Ly Kho')),
                ('thoigiantao', models.DateField()),
                ('thoigiannhanhang', models.DateField()),
                ('ghichu', models.CharField(default='.', max_length=200, verbose_name='Ghi Chú  ')),
                ('phanhoi', models.CharField(default='.', max_length=200, verbose_name='Phản Hồi  ')),
                ('kho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.khohang', verbose_name='Kho')),
                ('nhacungcap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.nhacungcap', verbose_name='Nhà cung cấp')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Tài Khoản')),
            ],
            options={
                'verbose_name': 'PHIẾU NHẬP XUẤT HÀNG ',
                'verbose_name_plural': 'PHIẾU NHẬP XUẤT HÀNG',
            },
        ),
        migrations.CreateModel(
            name='Nhapkho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noidung', models.JSONField()),
                ('tinhtrang_hoanthanh', models.BooleanField(verbose_name='Tình Trạng Hoàn Thành 100% ')),
                ('tinhtrang_treo', models.BooleanField(verbose_name='Tình Trạng Hoàn Thành < 100% ')),
                ('thoigiantao', models.DateField(auto_now_add=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.phieunhaphang', verbose_name='Số Phiếu Nhập Hàng')),
            ],
            options={
                'verbose_name': 'NHẬP KHO ',
                'verbose_name_plural': 'NHẬP KHO',
            },
        ),
        migrations.CreateModel(
            name='Nhaphang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soluong', models.IntegerField(blank=True, default=0, verbose_name='Số Lượng')),
                ('tinhtrang', models.BooleanField(verbose_name='Tình Trạng -( Check Nếu Hàng Đã Thực Nhập )')),
                ('hanghoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.hanghoa', verbose_name='Tên Hàng Hoá')),
                ('kho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.khohang')),
            ],
            options={
                'verbose_name': 'NHẬP HÀNG ',
                'verbose_name_plural': 'NHẬP HÀNG',
            },
        ),
        migrations.AddField(
            model_name='hanghoa',
            name='hangsx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.hangsx', verbose_name='Hãng Sản Xuất'),
        ),
        migrations.AddField(
            model_name='hanghoa',
            name='hemay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.hemay', verbose_name='Hệ Máy '),
        ),
        migrations.AddField(
            model_name='hanghoa',
            name='loaimay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.loaimay', verbose_name='Loại Máy '),
        ),
        migrations.AddField(
            model_name='hanghoa',
            name='nganhhang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khovan.nganhhang', verbose_name='Danh Mục'),
        ),
    ]
