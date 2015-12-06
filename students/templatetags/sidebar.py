from django import template
from students.models import Student, Group

register = template.Library()

@register.inclusion_tag("right_sidebar.html")
def show_sidebar():
    students = Student.objects.all().order_by('first_name')
    groups = Group.objects.all().order_by("title")
    return {'students': students, 'groups': groups}

