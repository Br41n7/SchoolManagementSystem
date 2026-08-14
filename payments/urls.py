from django.urls import path
from .views import payment_receipt, download_receipt

app_name = 'payments'

urlpatterns = [
    path('receipt/<str:ref_id>/', payment_receipt, name='payment_receipt'),
    path('receipt/<str:ref_id>/download/', download_receipt, name='download_receipt'),
]
