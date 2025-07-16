from payments.paystack import initialize_payment
from payments.utils import generate_ref, get_fee_amount
from payments.models import Payment
from .models import Hostel, Room, HostelApplication
from django.contrib.auth.decorators import login_required
from .forms import HostelApplicationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


@login_required
def apply_hostel(request):
    if request.method == 'POST':
        form = HostelApplicationForm(request.POST, user=request.user)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user
            application.status = 'pending'
            application.save()
            return redirect('hostel:payment_redirect', pk=application.pk)
    else:
        form = HostelApplicationForm(user=request.user)
    return render(request, 'hostel/apply.html', {'form': form})


@login_required
def my_hostel_view(request):
    try:
        application = HostelApplication.objects.get(
            student=request.user, status='approved')
    except HostelApplication.DoesNotExist:
        application = None
    return render(request, 'hostel/my_hostel.html', {'application': application})


def hostel_fee_payment(request):
    if request.method == 'POST':
        ref = generate_ref()
        amount = get_fee_amount('hostel')
        if not amount:
            return HttpResponse('Hostel payments is currently unavailable', status=403)

        Payment.objects.create(
            student=request.user,
            amount=amount,
            purpose='hostel',
            ref_id=ref,
            payment_method='paystack'
        )

        res = initialize_payment(request.user.email, amount, ref)
        if res.get('status'):
            return redirect(res['data']['authorization_url'])

    return render(request, 'hostel/pay.html')


def hostel_allocate(request):
    has_paid = Payment.objects.filter(
        student=request.user, purpose='hostel', status='paid').exists()
    if not has_paid:
        return redirect('hostel:pay_fee')
