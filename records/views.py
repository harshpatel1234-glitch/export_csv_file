from django.shortcuts import render

# Create your views here.
import csv
from django.http import HttpResponse

def export_students_csv(modeladmin, request, queryset):
    # Allow only superadmin
    if not request.user.is_superuser:
        return HttpResponse("❌ Only superadmin can export data")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'Email', 'Created At'])

    for student in queryset:
        writer.writerow([
            student.id,
            student.name,
            student.email,
            student.created_at
        ])

    return response

export_students_csv.short_description = "Export selected records to CSV"
