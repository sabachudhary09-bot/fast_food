from django.contrib import admin
from django.utils.html import format_html
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','id', 'category', 'size', 'price', 'is_popular', 'image_tag')
    list_filter = ('category', 'size', 'is_popular')
    search_fields = ('name',)

    # IMAGE PREVIEW
    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    image_tag.short_description = 'Image'