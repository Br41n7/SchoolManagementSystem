from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    def _str_(self):
        return self.username


class School(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='school/', blank=True, null=True)
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
        ordering = ['-start_date']

    def _str_(self):
        return self.name


class SystemSettings(models.Model):
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='system/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#0d6efd")
    footer_text = models.TextField(blank=True)
    allow_registration = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.site_name} Settings"
