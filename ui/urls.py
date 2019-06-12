from django.conf.urls import url

from .views import SetupView, DashboardView
from core.views import TeamCreate, TeamList, TeamDetail, TeamEdit, TeamDelete, Members

urlpatterns = [
    url(r'^setup', view=SetupView.as_view(), name='setup'),
    url(r'^overview', view=DashboardView.as_view(), name='overview'),
    url(r'^team/new$', view=TeamCreate.as_view(), name='newteam'),
    url(r'^teams$', view=TeamList.as_view(), name='teams'),
    url(r'^team/(?P<id>[\w-]+)$', view=TeamDetail.as_view(), name='teamdetail'),
    url(r'^team/edit/(?P<id>[\w-]+)$', view=TeamEdit.as_view(), name='teamedit'),
    url(r'^team/delete/(?P<name>[\w-]+)$', view=TeamDelete.as_view(), name='deleteteam'),
    url(r'^members$', view=Members.as_view(), name='members'),
]
