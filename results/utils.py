from django.db.models import Sum, F
from .models import CourseResult, CGPA


def calculate_gpa(student, session, semester):
    results = CourseResult.objects.filter(
        student=student, session=session, semester=semester)
    total_units = results.aggregate(total=Sum('course__unit'))['total'] or 0
    total_points = sum(r.point * r.course.unit for r in results)

    if total_units == 0:
        return 0.0
    return round(total_points / total_units, 2)


def update_cgpa(student):
    all_results = CourseResult.objects.filter(student=student)
    sessions = all_results.values_list('session', flat=True).distinct()
    all_cgpa = []

    total_units = 0
    total_points = 0
    for session in sessions:
        session_results = all_results.filter(session=session)
        session_units = session_results.aggregate(
            t=Sum('course__unit'))['t'] or 0
        session_points = sum(r.point * r.course.unit for r in session_results)

        total_units += session_units
        total_points += session_points

        gpa = round(session_points / session_units, 2) if session_units else 0
        cgpa = round(total_points / total_units, 2) if total_units else 0
        grade_class = get_class_from_cgpa(cgpa)
        CGPA.objects.update_or_create(
            student=student,
            session=session,
            defaults={'gpa': gpa, 'cgpa': cgpa, 'grade_class': grade_class}
        )


def get_class_from_cgpa(cgpa):
    if cgpa >= 4.5:
        return "First Class"
    elif cgpa >= 3.5:
        return "Second Class Upper"
    elif cgpa >= 2.5:
        return "Second Class Lower"
    elif cgpa >= 1.5:
        return "Third Class"
    else:
        return "Pass"
