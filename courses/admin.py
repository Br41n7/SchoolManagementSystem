from .models import Course, StudentCourseRegistration
from django.contrib import admin


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # list_display = ['code', 'title', 'unit', 'level',
    #                 'semester', 'session', 'compulsory']
    # list_filter = ['level', 'semester', 'session', 'compulsory']
    search_fields = ['code', 'title']


@admin.register(StudentCourseRegistration)
class StudentCourseRegistrationAdmin(admin.ModelAdmin):
    # list_display = ['student', 'course', 'semester', 'session', 'approved']
    # list_filter = ['semester', 'session', 'approved']
    search_fields = ['student_username', 'course_course_code']
