from django.urls import path
from .views import admission_apply, screening_dashboard,screening_list

urlpatterns = [
    path("apply/", admission_apply, name="admission_apply"),
    path("screening/", screening_dashboard, name="screening_dashboard"),
    path('screening/', screening_list, name='screening_list'),
    # path('screening/<int:pk>/update/', views.screening_update, name='screening_update'),

]
