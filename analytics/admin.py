from django.contrib import admin
from .models import SystemStat, ReportLog, ActivityLog


@admin.register(SystemStat)
class SystemStatAdmin(admin.ModelAdmin):
    list_display = ('school', 'date', 'total_applicants', 'total_students', 'total_courses', 'total_appeals')
    list_filter = ('school', 'date')
    search_fields = ('school__name',)
    ordering = ('-date',)


@admin.register(ReportLog)
class ReportLogAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'school', 'generated_by', 'generated_on')
    list_filter = ('school', 'generated_on')
    search_fields = ('report_type', 'school_name', 'generated_by_username')
    ordering = ('-generated_on',)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'school', 'action', 'timestamp', 'ip_address')
    list_filter = ('school', 'timestamp')
    search_fields = ('user__username', 'action')
    ordering = ('-timestamp',)
