from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, StudentCourseRegistration
from .forms import StudentCourseRegistrationForm
from django.contrib import messages
from payments.models import Payment
from payments.utils import generate_ref, get_fee_amount
from payments.paystack import initialize_payment
from django.http import HttpResponse


@login_required
def course_registration(request):
    student = request.user
    registered_courses = StudentCourseRegistration.objects.filter(
        student=student)

    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.student = student
            registration.save()
            messages.success(request, "Course registered successfully!")
            return redirect('courses:register')
    else:
        form = CourseRegistrationForm()
    has_paid = Payment.objects.filter(
        student=request.user, purpose='course', status='paid').exists()
    if not has_paid:
        return redirect('courses:pay_fee')
    context = {
        'form': form,
        'registered_courses': registered_courses,
    }
    return render(request, 'courses/register.html', context)


def course_fee_payment(request):
    if request.method == 'POST':
        ref = generate_ref()
        amount = get_fee_amount('course')
        if not amount:
            return HttpResponse('Course payments is currently unavailable', status=404)

        Payment.objects.create(
            student=request.user,
            amount=amount,
            purpose='course',
            ref_id=ref,
            payment_method='paystack'
        )

        res = initialize_payment(request.user.email, amount, ref)
        if res.get('status'):
            return redirect(res['data']['authorization_url'])

    return render(request, 'courses/pay.html')
