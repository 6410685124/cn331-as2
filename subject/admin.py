from django.contrib import admin

# Register your models here.
from .models import Class, Subject, Student

class classAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'semester', 'total_seats', 'remaining_seats','status')
    filter_horizontal = ('students',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id')

admin.site.register(Class, classAdmin)
admin.site.register(Subject)
admin.site.register(Student, StudentAdmin)