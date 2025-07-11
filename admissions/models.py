from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from django.db import models

# Create your models here.


class AdmissionApplication(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("screening", "Under Screening"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10,choices=[('Male','Male'),
                                                     ('Female','Female')])
    jamb_reg_number=models.CharField(max_length=20,unique=True)
    jamb_score=models.PositiveIntegerField()
    olevel_result=models.FileField(upload_to='olevels/')
    passport_photo=models.ImageField(upload_to='passports/')

    address = models.TextField()
    program = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    submitted_at = models.DateTimeField(default=timezone.now)
    is_notified = models.BooleanField(default=False)
    student_created = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk:
            old = AdmissionApplication.objects.get(pk=self.pk)
            if old.status != self.status and not self.is_notified:
                send_mail(
                    subject="Admission Status Update",
                    message=f"Dear {self.full_name}, your application status has changed to '{
                        self.status.title()}'.",
                    from_email="noreply@myschool.edu",
                    recipient_list=[self.email],
                    fail_silently=True,
                )
                self.is_notified = True
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.full_name} - {self.program} - {self.jamb_reg_number}"


class UploadedDocument(models.Model):
    application = models.ForeignKey(
        AdmissionApplication, on_delete=models.CASCADE, related_name="documents"
    )
    # e.g. 'Birth Certificate', 'O-Level Result'
    doc_type = models.CharField(max_length=50)

    def upload_to(instance, filename):
        return f"admissions/{instance.application.id}/{filename}"

    file = models.FileField(upload_to=upload_to)

    def _str_(self):
        return f"{self.doc_type} for {self.application.full_name}"
