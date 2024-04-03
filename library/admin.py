from django.contrib import admin
from .models import Book,Autor,BookingBook,Comment

admin.site.register(Book)
admin.site.register(Autor)
admin.site.register(BookingBook)
admin.site.register(Comment)