from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from qlns.models import Nhanvien
from qlns.resources import NhanvienResource
from datetime import datetime
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

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



admin.site.register(Permistions)
admin.site.register(Sett)