"""
Urls for sysadmin dashboard feature
"""
# pylint: disable=E1120

from django.conf.urls import patterns, url

from dashboard import sysadmin

urlpatterns = patterns(
    '',
    url(r'^$', sysadmin.Users.as_view(), name="sysadmin"),
    url(r'^courses/?$', sysadmin.Courses.as_view(), name="sysadmin_courses"),
    url(r'^staffing/?$', sysadmin.Staffing.as_view(), name="sysadmin_staffing"),
    url(r'^gitlogs/?$', sysadmin.GitLogs.as_view(), name="gitlogs"),
    url(r'^gitlogs/(?P<course_id>.+)$', sysadmin.GitLogs.as_view(),
        name="gitlogs_detail"),
)
