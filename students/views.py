from django.contrib.auth import get_user_model
from students.models import Student
from courses.models import CourseRegistration
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def dashboard(request):
    # Fetch distinct sessions and semesters from registrations
    sessions = CourseRegistration.objects.values_list("session", flat=True).distinct()
    semesters = CourseRegistration.objects.values_list("semester", flat=True).distinct()
    context = {
        "sessions": sorted(sessions, reverse=True),
        "semesters": sorted(semesters),
    }
    return render(request, "students/dashboard.html", context)


def calculate_cgpa(student):
    results = CourseRegistration.objects.filter(student=student, grade__isnull=False)
    total_units = sum(r.course.unit for r in results)
    total_points = sum(r.course.unit * r.point for r in results)
    return round(total_points / total_units, 2) if total_units else 0.0


@login_required
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    cgpa = calculate_cgpa(student)
    return render(
        request, "students/dashboard.html", {"student": student, "cgpa": cgpa}
    )


# class StudentProfile()


# create linked user
# User = get_user_model()
# # Create your views here.
# user = User.objects.create_user(
#     username=app.email,
#     email=app.email,
#     password=User.objects.make_random_password(),
# )
# student = Student.objects.create(
#     user=user,
#     full_name=app.full_name,
#     program=app.program,
# )
# app.student_created = True
# app.save()
# messages.success(request, f"Student profile created for {app.full_name}")
