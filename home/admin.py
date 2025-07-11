from django.contrib import admin
from .models import Feature, Testimonial, Client

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    readonly_fields = ('photo_preview',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.photo.url)
        return ""
    photo_preview.short_description = 'Photo Preview'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.logo.url)
        return ""
    logo_preview.short_description = 'Logo Preview'

