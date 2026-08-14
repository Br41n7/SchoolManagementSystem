from django.urls import path
from . import views

app_name = "hostel"

urlpatterns = [
    path('apply/', views.apply_hostel, name='apply'),
    path('my_hostel/', views.my_hostel_view, name='my_hostel'),
    path('pay/<int:pk>/', views.hostel_fee_payment, name='payment_redirect'),
]
