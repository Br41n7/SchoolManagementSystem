from .models import Payment
from .paystack import initialize_payment, verify_payment
from .utils import generate_ref
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required


def make_payment(request):
    if request.method == 'POST':
        purpose = request.POST.get('purpose')
        amount = float(request.POST.get('amount'))
        ref = generate_ref()

        payment = Payment.objects.create(
            student=request.user,
            amount=amount,
            purpose=purpose,
            ref_id=ref,
            payment_method='paystack'
        )

        res = initialize_payment(request.user.email, amount, ref)
        if res.get('status'):
            return redirect(res['data']['authorization_url'])

    return render(request, 'payments/pay.html')


def verify(request):
    ref = request.GET.get('reference')
    res = verify_payment(ref)
    if res['status'] and res['data']['status'] == 'success':
        Payment.objects.filter(ref_id=ref).update(status='paid')
    else:
        Payment.objects.filter(ref_id=ref).update(status='failed')
    return render(request, 'payments/verify.html', {'result': res})


def payment_receipt(request, ref_id):
    payment = get_object_or_404(Payment, ref_id=ref_id, student=request.user)
    return render(request, 'payments/receipt.html', {'payment': payment})
