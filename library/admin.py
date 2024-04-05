from django.contrib import admin
from .models import Student,Adress
# Register your models here.

@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ("id",'name',)
    list_display_links = ("id",'name',)
    search_fields =("name",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id",'first_name','last_name','status',"age","phone_number")
    list_display_links = ('id','first_name','last_name','status',"age","phone_number")
    search_fields = ('first_name','age','id')
    ordering = ('id',)
