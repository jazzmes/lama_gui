from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lama_gui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^monitor/', include('monitor.urls'))
    # url(r'^$', 'monitor.views.home', name='home'),
)
