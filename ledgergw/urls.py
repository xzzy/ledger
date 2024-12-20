from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from ledgergw.admin import admin
from ledgergw import api
from ledgergw import views
from ledger.accounts.views import logout
from ledger.urls import urlpatterns as ledger_patterns

# URL Patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^ledgergw/remote/user/(?P<ledgeremail>.+)/(?P<apikey>.+)/', api.user_info),
    url(r'^ledgergw/remote/userid/(?P<userid>[0-9]+)/(?P<apikey>.+)/', api.user_info_id),
    url(r'^ledgergw/remote/user-search/(?P<apikey>.+)/', api.user_info_search),
    url(r'^ledgergw/remote/groups/(?P<apikey>.+)/', api.group_info),
    url(r'^ledgergw/ip-check/', api.ip_check),
    url(r'^reports/$', views.ReportsView.as_view(), name='reports'),
    url(r'^logout/$', logout, name='logout' ),
] + ledger_patterns 


if settings.DEBUG:  # Serve media locally in development.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
