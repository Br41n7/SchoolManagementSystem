from django.urls import path
from .views import download_student_document

urlpatterns = [
    path('documents/download/<int:doc_id>/', download_student_document, name='download_student_document'),
    path('events-json/',views.events_json,name='events_json'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:pk>/update/', views.event_update, name='event_update'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
]

