from django.shortcuts import render
from django.http import HttpResponse

def student_page(request):
    return render(request, 'students.html')


def about_page(request):
    return render(request, 'student.html')
