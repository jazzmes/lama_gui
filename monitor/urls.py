from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from monitor import views

router = DefaultRouter()
router.register(r'api', views.ProviderAgentsAPIViewSet)

# urlpatterns = [
#     url(r'^$', views.home, name='home'),
#     url(r'^provider_agents', views.provider_agents, name='provider_agents'),
#     url(r'^api/$', views.ProviderAgentsAPIList.as_view(), name='provider_agents_api'),
#     url(r'^api/(?P<pk>[0-9]+)/$', views.ProviderAgentAPIDetail.as_view(), name='provider_agents_detail_api'),
#     url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^provider_agents', views.provider_agents, name='provider_agents'),
    # url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]
