from students.models import Student
from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    unit = models.PositiveIntegerField()
    level = models.IntegerField()

    def _str_(self):
        return f"{self.code} - {self.title}"


class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10)
    session = models.CharField(max_length=9)  # e.g. 2024/2025
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        unique_together = ("student", "course", "semester", "session")


# Create your models here.
