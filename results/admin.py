from django.contrib import admin
from .models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'session', 'semester', 'grade']
    list_filter = ['session', 'semester']
    search_fields = ['student_username', 'course_code']
