# Generated by Django 3.2.7 on 2021-09-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0010_xinphep_phongban'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanvien',
            name='diachihientai',
            field=models.CharField(default='', max_length=255, verbose_name='Địa chỉ Hiện Tại'),
        ),
        migrations.AddField(
            model_name='nhanvien',
            name='sos',
            field=models.IntegerField(default=0, verbose_name='Số Điện Thoại Khẩn Cấp'),
        ),
        migrations.AddField(
            model_name='nhanvien',
            name='tinhtranghonnhan',
            field=models.CharField(blank=True, choices=[('Độc Thân', 'Độc Thân'), ('Đã Kết Hôn', 'Đã Kết Hôn')], max_length=255, null=True, verbose_name='Tình Trạng Hôn Nhân '),
        ),
    ]