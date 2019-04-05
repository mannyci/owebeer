from django.conf.urls import url

from .views import overview, SetupView, DashboardView

urlpatterns = [
    url(r'^setup', view=SetupView.as_view(), name='setup'),
    url(r'^overview', view=DashboardView.as_view(), name='overview'),
]
