from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("staff", "Staff Member"),
        ("admin", "Administrator"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    # Add extra fields here as needed
    phone = models.CharField(max_length=20, blank=True, null=True)
    student_courses=models.ManyToManyField('courses.Course',blank='True',related_name='students')
    staff_courses=models.ManyToManyField('courses.Course',blank=True,related_name='staff_members')


    def _str_(self):
        return f"{self.user.username} - {self.get_role_display()}"


class School(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="school/", blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    established = models.DateField()

    def _str_(self):
        return self.name


class AcademicSession(models.Model):
    name = models.CharField(max_length=20)  # e.g. "2024/2025"
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_date"]

    def _str_(self):
        return self.name


class SystemSettings(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="system/", blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#0d6efd")
    footer_text = models.TextField(blank=True)
    allow_registration = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.site_name} Settings"
    class Meta:
        verbose_name="System Customization"
        verbose_name_plural="System Customizations"



class Event(models.Model):
    EVENT_TYPES = [
        ("class", "Class"),
        ("exam", "Exam"),
        ("holiday", "Holiday"),
        ("meeting", "Meeting"),
    ]
    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    # Optional: related to course or batch
    course = models.ForeignKey(
        "courses.Course", null=True, blank=True, on_delete=models.SET_NULL
    )

    def _str_(self):
        return f"{self.title} ({self.get_event_type_display()})"



User = get_user_model()

class StudentDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='student_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.title} ({self.user.username})"
