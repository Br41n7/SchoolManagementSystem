from .models import AdmissionApplication
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionForm, DocumentUploadForm
from .models import UploadedDocument


def admission_apply(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        files = request.FILES.getlist('file')
        doc_types = request.POST.getlist('doc_type')

        if form.is_valid():
            application = form.save()
            for file, doc_type in zip(files, doc_types):
                UploadedDocument.objects.create(
                    application=application, doc_type=doc_type, file=file)
            messages.success(request, 'Application submitted successfully.')
            return redirect('admission_apply')
    else:
        # Create your views here.
    form = AdmissionForm()
    return render(request, 'admissions/apply.html', {'form': form})


def is_staff(user):
    return user.is_authenticated and user.is_staff


@login_required
@user_passes_test(is_staff)
def screening_dashboard(request):
    applications = AdmissionApplication.objects.all().order_by('-submitted_at')

    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        new_status = request.POST.get('new_status')
        try:
            app = AdmissionApplication.objects.get(pk=app_id)
            app.status = new_status
            app.is_notified = False  # allow re-notification
            app.save()
            messages.success(request, f"Status updated to {
                             new_status.title()} for {app.full_name}")
        except:
            messages.error(request, "Failed to update application.")
            return HttpResponseRedirect(reverse('screening_dashboard'))

    return render(request, 'admissions/screening_dashboard.html',
                  {'applications': applications})
