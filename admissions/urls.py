from django.urls import path
from .views import apply, screening_dashboard,screening_list

app_name="admissions"

urlpatterns = [
    path("apply/", apply, name="apply"),
    path("screening/", screening_dashboard, name="screening_dashboard"),
    path('screening/', screening_list, name='screening_list'),
    # path('screening/<int:pk>/update/', views.screening_update, name='screening_update'),

]
