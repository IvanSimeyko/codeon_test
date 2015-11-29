# -*- coding: utf-8 -*-

from django.shortcuts import render
from models import Group, Student
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django import forms
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

#def group_list(request):
#    return render(request, 'students/group_list.html', {})


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupListView(ListView):
    """Groups List"""
    #queryset = Group.objects.all()
    model = Group
    paginate_by = 3
    context_object_name = 'groups'


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    context_object_name = 'group'
    #template_name = 'edit_course.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        response = super(GroupUpdateView, self).form_valid(form)
        messages.success(self.request, u'Данные группы %s были успешно изменены' % self.object.title)
        return response

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование группы'
        return context


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    context_object_name = 'course'
    template_name = 'students/group_form.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        response = super(GroupCreateView, self).form_valid(form)
        messages.success(self.request, u'Группв %s успешно добавлена' % self.object.title)
        return response

    def get_context_data(self, **kwargs):
        context = super(GroupCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание новой группы'
        return context