# Generated by Django 3.2.7 on 2021-09-29 07:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0012_alter_nhanvien_sos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chucvu_congviec',
            options={'verbose_name': 'NHÂN VIÊN CHỨC VỤs', 'verbose_name_plural': 'NHÂN VIÊN CHỨC VỤs'},
        ),
        migrations.AddField(
            model_name='tiemvecxincovid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tiemvecxincovid',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Luutamnhanvien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sdtcn', models.CharField(blank=True, default=' ', max_length=20, verbose_name='Điện Thoại Cá Nhân')),
                ('dcht', models.CharField(blank=True, default=' ', max_length=255, null=True, verbose_name='Địa chỉ hiện tại')),
                ('cmnd', models.CharField(blank=True, default=' ', max_length=255, null=True, verbose_name='Chứng Minh Nhân Dân')),
                ('file_cmnd_1', models.FileField(blank=True, null=True, upload_to='nhanvien/hosonhanvien/luutam', verbose_name='Mặt Trước Chứng Minh Nhân Dân')),
                ('file_cmnd_2', models.FileField(blank=True, null=True, upload_to='nhanvien/hosonhanvien/luutam', verbose_name='Mặt Sau Chứng Minh Nhân Dân')),
                ('ngaycap', models.DateField(blank=True, default=' ', max_length=20, null=True, verbose_name='Ngày Cấp Chứng Minh Nhân Dân')),
                ('noicap', models.CharField(blank=True, default=' ', max_length=20, null=True, verbose_name=' Nới Cấp Chứng Minh Nhân Dân')),
                ('duyet', models.BooleanField()),
                ('huy', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nhanvien', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qlns.nhanvien', verbose_name='Nhân Viên')),
            ],
            options={
                'verbose_name': 'DUYỆT CẬP NHẬT HỒ SƠ ',
                'verbose_name_plural': 'DUYỆT CẬP NHẬT HỒ SƠ ',
                'ordering': ['-id'],
            },
        ),
    ]