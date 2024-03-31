from django.shortcuts import render

def library_views(request):
    return render(request, "library.html")
