from django.contrib import admin
from BHcassper.models import *

from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ExportActionMixin
from import_export import resources
from BHcassper.resources  import BHcasperResource,BHcasperResourceout
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill
from imagekit.cachefiles import ImageCacheFile
from django.db.models.functions import Lower
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
# Register your models here.
import datetime

class SeriAdmin(ImportExportActionModelAdmin):
    list_display =('seri', 'admin_barcode','active','created_at')
    search_fields = ('seri',)
    list_per_page = 10
    list_editable =('active',)
    list_filter = (
       ('active'), ('created_at', DateRangeFilter),
    )
    resource_class = BHcasperResource
    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)
    def get_rangefilter_created_at_title(self, request, field_path):
        return 'Thời Gian Tạo'
    
    def admin_barcode(self, obj):
        return obj.admin_barcode

    admin_barcode.short_description = 'Barcode'
    admin_barcode.allow_tags = True
    
    

admin.site.register(Serial_Casper,SeriAdmin)


class Seri_outAdmin(ImportExportActionModelAdmin):
    list_display =('seri', 'admin_barcode','active','created_at')
    search_fields = ('seri',)
    list_per_page = 10
    list_editable =('active',)
    list_filter = (
       ('active'), ('created_at', DateRangeFilter),
    )
    resource_class = BHcasperResourceout
    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)
    def get_rangefilter_created_at_title(self, request, field_path):
        return 'Thời Gian Tạo'
    
    def admin_barcode(self, obj):
        return obj.admin_barcode

    admin_barcode.short_description = 'Barcode'
    admin_barcode.allow_tags = True
    
    

admin.site.register(Serial_Casper_out,Seri_outAdmin)