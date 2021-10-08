from import_export import fields, resources, widgets
from BHcassper.models import Serial_Casper, Serial_Casper_out


class BHcasperResource(resources.ModelResource):
    class Meta:
        model = Serial_Casper
        # skip_unchanged = True
        # report_skipped = False
        # field = ('seri','active','created_at')
        # export_order = ('seri','active', 'created_at')
        # exclude = ('id', 'barcode')
        
class BHcasperResourceout(resources.ModelResource):
    class Meta:
        model = Serial_Casper_out
        # skip_unchanged = True
        # report_skipped = False
        # field = ('seri','active','created_at')
        # export_order = ('seri','active', 'created_at')
        # exclude = ('id', 'barcode')
        