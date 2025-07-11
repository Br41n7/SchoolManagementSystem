from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Result

@login_required
def result_view(request):
    results = Result.objects.filter(student=request.user).order_by('session', 'semester')
    return render(request, 'results/result_view.html', {'results': results})
