from django.urls import path
from .views import student_page, about_page

urlpatterns = [
    path("students/", student_page),
    path("about/", about_page)
]