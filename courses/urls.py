from .views import course_registration, course_fee_payment
from django.urls import path

app_name = 'courses'
urlpatterns = [
    path("register/", course_registration, name="course_register"),
    path("pay/", course_fee_payment, name="pay_fee"),
]
