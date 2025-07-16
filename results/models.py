from courses.models import Course
from django.conf import settings
from django.db import models

GRADE_MAP = [
    (70, 'A', 5),
    (60, 'B', 4),
    (50, 'C', 3),
    (45, 'D', 2),
    (40, 'E', 1),
    (0,  'F', 0),
]


class CourseResult(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.FloatField()
    grade = models.CharField(max_length=2)
    point = models.PositiveSmallIntegerField()
    session = models.CharField(max_length=15)
    semester = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        for mark, grade, point in GRADE_MAP:
            if self.score >= mark:
                self.grade = grade
                self.point = point
                break
        super().save(*args, **kwargs)

    def _str_(self):
        return f"{self.student} - {self.course.code}: {self.grade}"


class CGPA(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.CharField(max_length=15)
    gpa = models.FloatField()
    cgpa = models.FloatField()
    grade_class = models.CharField(max_length=30)

    def _str_(self):
        return f"{self.student} - CGPA: {se.cgpa}"
