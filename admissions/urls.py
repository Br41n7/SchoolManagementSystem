from django.urls import path
from .views import admission_apply, screening_dashboard

urlpatterns = [
    path('apply/', admission_apply, name='admission_apply'),
    path('screening/', screening_dashboard, name='screening_dashboard'),
]
