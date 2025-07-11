from django.http import FileResponse, Http404,JsonResponse
from .models import StudentDocument,Event
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm

@login_required
def download_student_document(request, doc_id):
    document = get_object_or_404(StudentDocument, id=doc_id)
    if document.user != request.user:
        raise Http404("You do not have permission to access this file.")
    response = FileResponse(document.file.open('rb'), as_attachment=True, filename=document.file.name)
    return response

@login_required
def events_json(request):
    user = request.user
    events = Event.objects.filter(end_time__gte=now())

    if user.is_staff:
        # Staff sees all events or only those related to courses they teach
        events = events.filter(course__in=user.staff_courses.all())  # assuming staff_courses relation
    else:
        # Students see events related to their courses
        events = events.filter(course__in=user.student_courses.all())  # assuming student_courses relation

    data = [{
        'id': e.id,
        'title': e.title,
        'start': e.start_time.isoformat(),
        'end': e.end_time.isoformat(),
        'type': e.event_type,
    } for e in events]

    return JsonResponse(data, safe=False)



@login_required
def event_create(request):
    if not request.user.is_staff:
        return redirect('events_json')  # Only staff can create events

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('events_json')
    else:
        form = EventForm()

    return render(request, 'core/event_form.html', {'form': form})

@login_required
def event_update(request, pk):
    if not request.user.is_staff:
        return redirect('events_json')
    event = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events_json')
    else:
        form = EventForm(instance=event)

    return render(request, 'core/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    if not request.user.is_staff:
        return redirect('events_json')
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('events_json')

    return render(request, 'core/event_confirm_delete.html', {'event': event})
