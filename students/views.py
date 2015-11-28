from django.shortcuts import render


def group_list(request):
    return render(request, 'students/group_list.html', {})