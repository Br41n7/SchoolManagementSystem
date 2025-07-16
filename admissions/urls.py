from django.urls import path
from .views import apply, screening_dashboard, screening_list, admission_fee_payment
app_name = "admissions"

urlpatterns = [
    path("apply/", apply, name="apply"),
    path("screening/", screening_dashboard, name="screening_dashboard"),
    path('screening/', screening_list, name='screening_list'),
    path('pay/', admission_fee_payment, name='pay_fee'),

]
