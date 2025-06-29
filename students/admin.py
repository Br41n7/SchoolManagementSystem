from .models import Student
from django.contrib import admin


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'program', 'level', 'matric_no']
    search_fields = ['full_name', 'matric_no']
