from django.conf.urls import include, url, patterns
from django.contrib import admin
import settings
from students import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'student_root.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.GroupListView.as_view(), name='group_list'),
    url(r'^group/', include('students.urls', namespace="group")),
    url(r'^student/', include('students.urls_student', namespace="student")),
    url(r'^auth/', include('loginsys.urls', namespace="loginsys")),
    url(r'^contact/', include('contacts.urls', namespace="contacts")),
]


if settings.SERVE_MEDIA:
    urlpatterns += patterns(
        '',
        url(r'^photos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )