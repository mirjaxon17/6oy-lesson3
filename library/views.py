from django.shortcuts import render

def books_page(request):
    return render(request,'library.html')


def landing_page(request):
    return render(request, 'librarys.html')