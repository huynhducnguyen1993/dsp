# Generated by Django 3.2.7 on 2021-10-04 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qlns', '0018_alter_chucvu_congviec_nhanvien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chucvu_congviec',
            name='nhanvien',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='qlns.nhanvien', verbose_name='Nhân Viên'),
        ),
    ]
