from django.conf.urls import include, url, patterns
from django.contrib import admin
import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'student_root.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('students.urls')),
    url(r'^group/', include('students.urls', namespace="group")),
]


if settings.SERVE_MEDIA:
    urlpatterns += patterns(
        '',
        url(r'^photos/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )