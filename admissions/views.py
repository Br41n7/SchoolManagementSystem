from payments.paystack import initialize_payment
from payments.utils import generate_ref, get_fee_amount
from payments.models import Payment, FeeConfig
from .models import AdmissionApplication, UploadedDocument
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
# ,staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionForm  # DocumentUploadForm


def admission_fee_payment(request):
    if request.method == 'POST':
        ref = generate_ref()
        amount = get_fee_amount('admission')
        if not amount:
            return HttpResponse("screenform payments is currently unavailable", status=404)

        Payment.objects.create(
            student=request.user,
            amount=amount,
            purpose='admission',
            ref_id=ref,
            payment_method='paystack'
        )

        response = initialize_payment(request.user.email, amount, ref)
        if response.get('status'):
            return redirect(response['data']['authorization_url'])

    return render(request, 'admissions/payment_prompt.html')


def apply(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        files = request.FILES.getlist("file")
        # doc_types = request.POST.getlist("doc_type")

        if form.is_valid():
            application = form.save()
            # for file, doc_type in zip(files, doc_types):
            #     UploadedDocument.objects.create(
            #         application=application, doc_type=doc_type, file=file
            #     )
            messages.success(request, "Application submitted successfully.")
            return redirect("apply")
    else:
        form = AdmissionForm()
    return render(request, "apply.html", {"form": form})
    has_paid = Payment.objects.filter(
        student=request.user,
        purpose='admission',
        status='paid'
    ).exists()
    if not has_paid:
        return redirect('admissions:pay_fee')


def is_staff(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_staff)
def screening_dashboard(request):
    applications = AdmissionApplication.objects.all().order_by("-submitted_at")

    if request.method == "POST":
        app_id = request.POST.get("app_id")
        new_status = request.POST.get("new_status")
        try:
            app = AdmissionApplication.objects.get(pk=app_id)
            app.status = new_status
            app.is_notified = False  # allow re-notification
            app.save()
            messages.success(
                request,
                f"Status updated to {
                    new_status.title()} for {app.full_name}",
            )
        except:
            messages.error(request, "Failed to update application.")
            return HttpResponseRedirect(reverse("screening_dashboard"))

    return render(
        request, "admissions/screening_dashboard.html", {
            "applications": applications}
    )

# @staff_member_required


@login_required
def screening_update(request, pk):
    app = get_object_or_404(AdmissionApplication, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['Pending', 'Accepted', 'Rejected']:
            app.screening_status = status
            app.save()
            messages.success(request, f"{app.full_name}'s status updated.")
        return redirect('admission:screening_list')
    return render(request, 'admission/screening_update.html', {'app': app})

# @staff_member_required


@login_required
def screening_list(request):
    applications = AdmissionApplication.objects.all().order_by('-submitted_at')
    return render(request, 'admission/screening_list.html', {'applications': applications})
