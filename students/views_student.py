# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from models import Group, Student
from django import forms
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    context_object_name = 'student'
    template_name = 'students/group_form.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        response = super(StudentUpdateView, self).form_valid(form)
        messages.success(self.request, u'Данные студента %s были успешно изменены' % self.object.first_name)
        return response

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование данных студента'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('group_list')
    template_name = 'students/group_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        response = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.warning(request, u"Студент %s был успешно удален" % self.object.first_name)
        return response

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['page_title'] = u'Удаление данных о студенте %s %s' % (self.object.first_name, self.object.last_name)
        return context


class StudentListView(ListView):
    model = Student
    paginate_by = 5
    #template_name = 'students/group_detail.html'
    context_object_name = 'students'