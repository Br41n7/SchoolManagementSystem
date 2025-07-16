from django.urls import path
from . import views

app_name = 'results'

urlpatterns = [
    path('', viewsresult_view, name='view'),
    path('download/', views.download_results_pdf, name='download'),
]
