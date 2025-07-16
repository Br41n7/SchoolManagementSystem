from .models import CourseResult, CGPA
from django.contrib import admin


@admin.register(CourseResult)
class CourseResultAdmin(admin.ModelAdmin):
    # list_display = ('student', 'course', 'score', 'grade',
    #                 'point', 'session', 'semester')
    # list_filter = ('semester', 'session', 'grade')
    search_fields = ('student_username', 'course_code')


@admin.register(CGPA)
class CGPAAdmin(admin.ModelAdmin):
    # list_display = ('student', 'session', 'gpa', 'cgpa', 'grade_class')
    search_fields = ('student_username', 'student_email',
                     'course_title', 'course_code')
    # autocomplete_fields = ['student', 'course']
