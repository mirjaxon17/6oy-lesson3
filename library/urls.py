from django.urls import path
from .views import library_views


urlpatterns = [
    path("library/", library_views)
]