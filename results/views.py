import weasyprint
from django.template.loader import get_template
from django.http import HttpResponse
from .utils import update_cgpa
from .models import CourseResult
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def view_results(request):
    student = request.user
    results = CourseResult.objects.filter(
        student=student).select_related('course')

    update_cgpa(student)

    context = {
        'results': results,
        'student': student,
    }
    return render(request, 'results/view_results.html', context)


@login_required
def download_results_pdf(request):
    student = request.user
    results = CourseResult.objects.filter(
        student=student).select_related('course')

    template = get_template('results/pdf_template.html')
    html = template.render({'results': results, 'student': student})
    pdf = weasyprint.HTML(string=html).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{
        student.username}_results.pdf"'
    return response
