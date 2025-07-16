from django.urls import Path
from . import views

app_name = "hostel"

urlspatterns = [
    path('apply/', views.apply_hostel, name='apply'),
    path('my_hostel/', views.my_hostel_view, name='my_hostel'),
    path('pay/<int:pk>/', views.payment_redirect, name='payment_redirect'),

]
