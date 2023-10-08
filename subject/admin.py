from django.contrib import admin

# Register your models here.
from .models import Class, Subject, Student

class classAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_seats', 'remaining_seats', 'semester', 'status')
    filter_horizontal = ('students',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'year')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

admin.site.register(Class, classAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)