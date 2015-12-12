from django.contrib import admin
from students.models import Student, Group


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'student_group']
    search_fields = ['last_name', 'first_name', 'student_group', 'birthday']
    list_filter = ['last_name', 'first_name', 'student_group']
    #fieldsets =
    #filter_horizontal = ('student_group',)


class StudentInline(admin.TabularInline):
    model = Student


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'starosta']
    search_fields = ['title', 'starosta']
    list_filter = ['title', 'starosta']
    inlines = [ StudentInline, ]




admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
