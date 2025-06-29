from .models import User, School, AcademicSession, SystemSettings
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_student',
                    'is_staff_member', 'is_superadmin', 'is_active')
    list_filter = ('is_student', 'is_staff_member',
                   'is_superadmin', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {
            'fields': ('is_student', 'is_staff_member', 'is_superadmin'),
        }),
    )


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'established')
    search_fields = ('name', 'short_name')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" height="40">'
        return "-"
    logo_preview.allow_tags = True
    logo_preview.short_description = 'Logo'


@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'is_current')
    list_editable = ('is_current',)
    ordering = ('-start_date',)


@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'school', 'allow_registration')
    readonly_fields = ('logo_preview',)

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" height="40">'
        return "-"
    logo_preview.allow_tags = True
    logo_preview.short_description = 'Logo Preview'
