from django.contrib import admin
from merch.models import Merch, MerchGallery


class MerchGalleryInline(admin.TabularInline):
    merch = 'product'
    model = MerchGallery
    readonly_fields = ('image_tag',)


class MerchAdmin(admin.ModelAdmin):
    inlines = [MerchGalleryInline, ]
    list_display = ('name', 'price', 'availability')
    ordering = ('availability',)


admin.site.register(Merch, MerchAdmin)
