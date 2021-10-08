from django.db import models
from django.contrib.auth import *
from django.contrib import admin
from django.db.models.base import ModelState
from django.db.models.fields import BooleanField
from qlns.models import *
from django.db.models.fields.related import OneToOneField
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser,User
from ckeditor.fields import *
from ckeditor_uploader.fields import *
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

# Create your models here.

class Serial_Casper(models.Model):
    seri = models.CharField(default="" ,max_length=200,null=True,blank=True)
    barcode = models.ImageField(upload_to='images/', blank=True)
    active = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        ordering =['active']
        verbose_name = "ĐẦU VÀO "
        verbose_name_plural = 'ĐẦU VÀO'

    def __int__(self):
        return self.seri
    @property
    def admin_barcode(self):
        if self.barcode:
            return mark_safe('<img src="{}" width="420" height="200" />'.format(self.barcode.url))
        return ""
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('code128')
        ean = EAN(f'{self.seri}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.seri}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)


class Serial_Casper_out(models.Model):
    seri = models.CharField(default="" ,max_length=200,null=True,blank=True)
    barcode = models.ImageField(upload_to='images/', blank=True)
    active = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        ordering =['active']
        verbose_name = "ĐẦU RA "
        verbose_name_plural = 'ĐẦU RA'

    def __int__(self):
        return self.seri
    @property
    def admin_barcode(self):
        if self.barcode:
            return mark_safe('<img src="{}" width="420" height="200" />'.format(self.barcode.url))
        return ""
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('code128')
        ean = EAN(f'{self.seri}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{self.seri}.png', File(buffer), save=False)
        return super().save(*args, **kwargs)