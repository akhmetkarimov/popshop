from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from . import models
from . import resources

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )

# ASC A-Z 0-9 (name)
# DESC Z-A 9-0 (-name)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_img')
    search_fields = ('name', )
    ordering = ('name', )

    def show_img(self, obj):
        return mark_safe(f'<img src="/media/{obj.img}" width="80" height="80">')
    # string -> html tag
    show_img.__name__ = 'Img'


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_img')
    search_fields = ('name', )
    ordering = ('name', )

    def show_img(self, obj):
        return mark_safe(f'<img src="/media/{obj.img}" width="80" height="80">')
    show_img.__name__ = 'Img'

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_img')
    search_fields = ('name', )
    ordering = ('name', )

    def show_img(self, obj):
        return mark_safe(f'<img src="/media/{obj.img}" width="80" height="80">')
    show_img.__name__ = 'Img'

class VendorAdmin(ImportExportModelAdmin):
    resource_class = resources.VendorResource
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    ordering = ('name', )

# @admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )
    filter_horizontal = ('collection',)

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.Catalog, CatalogAdmin)
admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Vendor, VendorAdmin)