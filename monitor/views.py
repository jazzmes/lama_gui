from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import DjangoModelPermissions
from monitor.models import Dispatcher, ProviderAgent
from monitor.serializers import ProviderAgentSerializer

def home(request):
    return render(request, 'home.html')


def provider_agents(request):
    # get first dispatcher
    disp = Dispatcher.objects.first()

    # if not disp:
    #     error = "No dispatcher in DB"

    # if disp.actions.

    # if last time they were loaded was recent
    # load from db (our cache)
    # else ask dispatcher

    return render(request, 'monitor/provider_agents.html')


class ProviderAgentsAPIViewSet(viewsets.ModelViewSet):
    """
    List all or create, retrieve, update or delete a provider agent.
    """

    queryset = ProviderAgent.objects.all()
    serializer_class = ProviderAgentSerializer
    permission_classes = (DjangoModelPermissions, )

