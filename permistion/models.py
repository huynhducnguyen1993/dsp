
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
from io import BytesIO, open_code
from django.core.files import File
from PIL import Image, ImageDraw
from django.conf import settings
from datetime import date

class Permistions(models.Model):
    chucnangapp = models.CharField(default="",max_length=255,verbose_name="Ten app_chuc nang ")
    username = models.ManyToManyField(User)
    class Meta:
        verbose_name = "Permistions "
        verbose_name_plural = 'Permistions'

    def __str__(self):
        return self.chucnangapp
class Sett(models.Model):
    tenchucnang  =  models.CharField(default="",max_length=255,verbose_name="Ten chuc nang ")
    noidung = models.TextField(default="",max_length=1000,verbose_name="Noi Dung")
    class Meta:
        verbose_name = "Cai Dat  "
        verbose_name_plural = 'Cai Dat'

    def __str__(self):
        return self.tenchucnang

 