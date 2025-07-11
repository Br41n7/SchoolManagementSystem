from .views import course_register,enter_results,download_result
from django.urls import path


urlpatterns = [
    path("register/", course_register, name="course_register"),
    path("results/entry/", enter_results, name="enter_results"),
    path("results/download/",download_result,name="download_result"),
]
