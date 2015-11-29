from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GroupListView.as_view(), name='group_list'),
    url(r'^edit/(?P<pk>\d+)/$', views.GroupUpdateView.as_view(), name='edit_group'),
]
