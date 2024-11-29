from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'seller', 'price', 'category', 'condition', 'created_at', 'college')
    search_fields = ('title', 'seller__username', 'description', 'category', 'college__name')
    list_filter = ('category', 'condition', 'created_at', 'college')
    readonly_fields = ('created_at',)  # Make 'created_at' read-only for safety

    # Adding image preview
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;">'
        return "No Image"
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True  # Required for rendering HTML
