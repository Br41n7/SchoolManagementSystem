from .models import AdmissionApplication, UploadedDocument
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test #,staff_member_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionForm, DocumentUploadForm

def apply(request):
    if request.method == "POST":
        form = AdmissionForm(request.POST)
        files = request.FILES.getlist("file")
        doc_types = request.POST.getlist("doc_type")

        if form.is_valid():
            application = form.save()
            for file, doc_type in zip(files, doc_types):
                UploadedDocument.objects.create(
                    application=application, doc_type=doc_type, file=file
                )
            messages.success(request, "Application submitted successfully.")
            return redirect("admission_apply")
    else:
        form = AdmissionForm()
    return render(request, "admissions/apply.html", {"form": form})


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
        request, "admissions/screening_dashboard.html", {"applications": applications}
    )

#@staff_member_required
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

#@staff_member_required
@login_required
def screening_list(request):
    applications = AdmissionApplication.objects.all().order_by('-submitted_at')
    return render(request, 'admission/screening_list.html', {'applications': applications})
