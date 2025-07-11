from django.contrib.admin.views.decorators import staff_member_required
from .models import Course, CourseRegistration
from django.contrib import messages
from students.models import Student
from .forms import CourseRegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .utils import render_to_pdf

@login_required
def course_register(request):
    student = Student.objects.get(user=request.user)

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST, student=student)
        if form.is_valid():
            semester = form.cleaned_data['semester']
            session = form.cleaned_data['session']
            courses = form.cleaned_data['courses']

            for course in courses:
                CourseRegistration.objects.get_or_create(
                    student=student,
                    course=course,
                    semester=semester,
                    session=session
                )
            messages.success(request, 'Courses registered successfully.')
            return redirect('student_dashboard')
    else:
        # Create your views here.
       form = CourseRegistrationForm(student=student)
    return render(request, 'courses/register.html', {'form': form})


@login_required
def registered_courses(request):
    student = Student.objects.get(user=request.user)
    registrations = CourseRegistration.objects.filter(
        student=student).select_related('course')
    return render(request, 'courses/registered_courses.html', {'registrations': registrations})


@staff_member_required
def enter_results(request):
    courses = Course.objects.all()
    selected_course = request.GET.get('course')

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('grade_'):
                reg_id = key.split('_')[1]
                try:
                    reg = CourseRegistration.objects.get(id=reg_id)
                    reg.grade = value.upper()
                    reg.point = grade_to_point(value.upper())
                    reg.save()
                except:
                    continue
        messages.success(request, "Results updated.")
        return redirect(request.path + f"?course={selected_course}")

    registrations = CourseRegistration.objects.filter(
        course__id=selected_course) if selected_course else []

    return render(request, 'courses/enter_results.html', {
        'courses': courses,
        'selected_course': selected_course,
        'registrations': registrations
    })


@login_required
def download_result(request):
    student = Student.objects.get(user=request.user)
    session = request.GET.get('session')
    semester = request.GET.get('semester')

    filters = {'student': student}
    if session:
        filters['session'] = session
    if semester:
        filters['semester'] = semester

    records = CourseRegistration.objects.filter(**filters).select_related('course')
    cgpa = calculate_cgpa_for(records)
    context = {
        'student': student,
        'records': records,
        'cgpa': cgpa,
        'session': session,
        'semester': semester
    }
    return render_to_pdf('courses/result_pdf.html', context)
