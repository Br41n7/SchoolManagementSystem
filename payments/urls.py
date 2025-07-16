from .views import payment_receipt
fron django.urls import path

urlpatterns = [
    path('receipt/<str:ref_id>/', payment_receipt, name='payment_receipt'),
    path('receipt/<str:ref_id>/apply/',
         download_receipt, name='download_receipt'),
]
