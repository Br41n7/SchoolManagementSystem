from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SystemStat, ReportLog, ActivityLog
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    school = request.user.school  # assuming User model has school relation
    stats = SystemStat.objects.filter(school=school).order_by('-date')[:30]  # Last 30 days
    context = {'stats': stats}
    return render(request, 'analytics/dashboard.html', context)


@login_required
def report_logs(request):
    school = request.user.school
    logs_list = ReportLog.objects.filter(school=school).order_by('-generated_on')
    paginator = Paginator(logs_list, 10)  # 10 per page
    page_number = request.GET.get('page')
    logs = paginator.get_page(page_number)

    context = {'logs': logs}
    return render(request, 'analytics/report_logs.html', context)


@login_required
def activity_logs(request):
    school = request.user.school
    activities_list = ActivityLog.objects.filter(school=school).order_by('-timestamp')
    paginator = Paginator(activities_list, 20)
    page_number = request.GET.get('page')
    activities = paginator.get_page(page_number)

    context = {'activities': activities}
    return render(request, 'analytics/activity_logs.html', context)


@login_required
def report_detail(request, report_id):
    school = request.user.school
    report = get_object_or_404(ReportLog, id=report_id, school=school)

    context = {'report': report}
    return render(request, 'analytics/report_detail.html', context)
