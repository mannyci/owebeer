"""
owebeer URL Configuration
"""

from django.conf.urls import url, include
from django.shortcuts import redirect
from django.contrib import admin
from django.conf import settings
from ui.utils import needs_setup

# Redirect Index to ui or run first setup
def index(request):
	if needs_setup():
		return redirect('ui:welcome')
	else:
		return redirect('ui:overview')

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^', include(('ui.urls', 'ui'), namespace='ui')),
    url(r'^', include(('account.urls', 'account'), namespace='account')),
    url(r'^admin/', admin.site.urls),
	url(r'^api/', include(('rest_framework.urls', 'api'), namespace='api'))
]

if settings.SETTINGS_MODULE == 'settings.development':
    try:
        import debug_toolbar
        urlpatterns += [
            # for Django version 2.0
            # path('__debug__/', include(debug_toolbar.urls)),

            # TODO: this is the Django < 2.0 version, REMOVEME
            url(r'^__debug__/', include(debug_toolbar.urls))
        ]
    except ImportError:
        pass