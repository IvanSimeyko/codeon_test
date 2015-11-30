from django.shortcuts import render, redirect
from models import Group, Student
from django import forms
from django.contrib import messages
from django.views.generic.detail import DetailView


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'


    #def get_context_data(self, **kwargs):
     #   context = super(StudentDetailView, self).get_context_data(**kwargs)
      #  group = self.get_object()
       # context['students'] = group.student_set.all()
        #return context