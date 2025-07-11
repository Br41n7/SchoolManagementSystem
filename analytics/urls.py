from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reports/', views.report_logs, name='report_logs'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),
    path('activities/', views.activity_logs, name='activity_logs'),
]
