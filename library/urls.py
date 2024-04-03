from django.urls import path
from .views import landing_page,books_page


urlpatterns = [
    path('landing/', landing_page),
    path('books/', books_page)
]