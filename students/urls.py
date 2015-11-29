from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GroupListView.as_view(), name='group_list'),
]
