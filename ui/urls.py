from django.conf.urls import url

from .views import overview, SetupView, DashboardView

urlpatterns = [
    url(r'^setup', view=SetupView.as_view(), name='setup'),
]
