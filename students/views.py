from django.contrib.auth import get_user_model
from students.models import Student
from courses.models import StudentCourseRegistration
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    sessions = StudentCourseRegistration.objects.values_list(
        "session", flat=True).distinct()
    semesters = StudentCourseRegistration.objects.values_list(
        "semester", flat=True).distinct()
    context = {
        "sessions": sorted(sessions, reverse=True),
        "semesters": sorted(semesters),
    }
    return render(request, "dashboard.html", context)


def calculate_cgpa(student):
    results = StudentCourseRegistration.objects.filter(
        student=student, grade__isnull=False)
    total_units = sum(r.course.unit for r in results)
    total_points = sum(r.course.unit * (r.point if hasattr(r, 'point') else 0) for r in results)
    return round(total_points / total_units, 2) if total_units else 0.0


@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    cgpa = calculate_cgpa(student)
    return render(
        request, "dashboard.html", {"student": student, "cgpa": cgpa}
    )
