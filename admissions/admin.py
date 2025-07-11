from .models import AdmissionApplication, UploadedDocument
from django.contrib import admin

# Register your models here.


class UploadedDocumentInline(admin.TabularInline):
    model = UploadedDocument
    extra = 0


@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "program",
        "status",
        "jamb_reg_number",
        "submitted_at",
        "is_notified",
    )
    list_filter = ("status", "program")
    search_fields = ("full_name", "email","jamb_reg_number")
    inlines = [UploadedDocumentInline]
    actions = ["mark_screened", "mark_accepted", "mark_rejected"]

    def mark_screened(self, request, queryset):
        queryset.update(status="screening")

    mark_screened.short_description = "Mark selected as Under Screening"

    def mark_accepted(self, request, queryset):
        queryset.update(status="accepted")

    mark_accepted.short_description = "Mark selected as Accepted"

    def mark_rejected(self, request, queryset):
        queryset.update(status="rejected")

    mark_rejected.short_description = "Mark selected as Rejected"


@admin.register(UploadedDocument)
class UploadedDocumentAdmin(admin.ModelAdmin):
    list_display = ("application", "doc_type", "file")
