from django.shortcuts import render
from models import Group, Student
from django.views.generic.list import ListView


#def group_list(request):
#    return render(request, 'students/group_list.html', {})

class GroupListView(ListView):
    """Groups List"""
    #queryset = Group.objects.all()
    model = Group
    paginate_by = 3
    context_object_name = 'groups'
