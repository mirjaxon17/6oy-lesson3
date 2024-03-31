from django.urls import path
from .views import student_vievs

urlpatterns = [
    path("students/", student_vievs)
]