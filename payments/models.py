from django.db import models
from django.conf import settings


class Payment(models.Model):
    METHOD_CHOICES = [('paystack', 'Paystack'), ('stripe', 'Stripe')]
    STATUS_CHOICES = [('pending', 'Pending'),
                      ('paid', 'Paid'), ('failed', 'Failed')]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.CharField(max_length=100)  # e.g., 'admission', 'hostel'
    ref_id = models.CharField(max_length=100, unique=True)
    payment_method = models.CharField(max_length=50, choices=METHOD_CHOICES)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.student.username} - {self.purpose} - {self.status}"


class FeeConfig(models.Model):
    PURPOSE_CHOICES = [
        ('admission', 'Admission'),
        ('hostel', 'Hostel'),
        ('course', 'Course Registration'),
    ]

    purpose = models.CharField(
        max_length=30, choices=PURPOSE_CHOICES, unique=True, help_text='e.g hostel,course,admission. etc')
    label = models.CharField(
        max_length=100, help_text='user-friendly name e.g hostel accomodation fee')
    amount = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.purpose.title()} Fee - ₦{self.amount}"
