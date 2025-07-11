from django.db import models
from core.models import UserProfile
from courses.models import Course

class Result(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.CharField(max_length=20)
    semester = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=2)
    remark = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ('student', 'course', 'session', 'semester')

    def _str_(self):
        return f"{self.student} - {self.course} ({self.grade})"
