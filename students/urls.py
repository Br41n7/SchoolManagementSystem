from .views import student_dashboard
from django.urls import path
from courses.views import course_registration
# from results.views import view_result

urlpatterns = [
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('student/register_course/', course_registration, name='register_course'),
    # path('student/results/', view_result, name='view_results'),
    # path('student/results/appeal/<int:course_id>/', result_appeal, name='result_appeal'),
]
