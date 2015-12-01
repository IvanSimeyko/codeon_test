# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from models import Group, Student
from django import forms
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy


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
