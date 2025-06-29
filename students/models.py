from django.utils.crypto import get_random_string
from django.conf import settings
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    program = models.CharField(max_length=100)
    level = models.IntegerField(default=100)
    matric_no = models.CharField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.matric_no:
            prefix = self.program[:3].upper()
            unique = get_random_string(length=5).upper()
            self.matric_no = f"{prefix}/{self.level}/{unique}"
        super().save(*args, **kwargs)

    def _str_(self):
        return self.full_name
