from django.contrib import admin

# Register your models here.
from .models import Student
from .views import export_students_csv

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    actions = [export_students_csv]
