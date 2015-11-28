from django.contrib import admin
from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'student_group']
    search_fields = ['last_name', 'first_name', 'student_group', 'birthday']
    list_filter = ['last_name', 'first_name', 'student_group']
    #fieldsets =
    #filter_horizontal = ('student_group',)


admin.site.register(Student, StudentAdmin)