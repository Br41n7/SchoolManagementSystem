from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course, Student
from core.models import School


class SystemStat(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_applicants = models.PositiveIntegerField(default=0)
    total_students = models.PositiveIntegerField(default=0)
    total_courses = models.PositiveIntegerField(default=0)
    total_appeals = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('school', 'date')
        ordering = ['-date']

    def _str_(self):
        return f"{self.school.name} stats on {self.date}"


class ReportLog(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    generated_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    report_type = models.CharField(max_length=100)
    generated_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='reports/', blank=True, null=True)

    def _str_(self):
        return f"{self.report_type} - {self.school} - {self.generated_on.strftime('%Y-%m-%d')}"


class ActivityLog(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def _str_(self):
        return f"{self.user} - {self.action} at {self.timestamp}"
