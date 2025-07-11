from django.urls import path
from .views import result_view

app_name = 'results'

urlpatterns = [
    path('', result_view, name='view'),
]
