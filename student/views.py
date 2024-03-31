from django.shortcuts import render

def student_vievs(request):
    return render(request, "students.html")
