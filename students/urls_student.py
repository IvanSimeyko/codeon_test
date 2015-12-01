from django.conf.urls import url
from . import views_student

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views_student.StudentDetailView.as_view(), name='description_student'),
    url(r'^edit/(?P<pk>\d+)/$', views_student.StudentUpdateView.as_view(), name='edit_student'),
    url(r'^delete/(?P<pk>\d+)/$', views_student.StudentDeleteView.as_view(), name='delete_student'),
]
