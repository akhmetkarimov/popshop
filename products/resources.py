from import_export import resources
from . import models

class VendorResource(resources.ModelResource):
    class Meta:
        model = models.Vendor
        exclude = ('id',)
        import_id_fields = ('name', 'code')
        skip_unchanged = True
        report_skipped = True
        chunk_size = 1000