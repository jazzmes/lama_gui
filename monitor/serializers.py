from rest_framework import serializers
from monitor.models import ProviderAgent


class ProviderAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderAgent
        fields = ('id', 'ip_address', 'agent_id')
