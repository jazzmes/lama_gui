from django.db import models
from django.utils import timezone


class Dispatcher(models.Model):
    ip_address = models.GenericIPAddressField("IP Address")

    def __str__(self):
        return self.ip_address


class ProviderAgent(models.Model):
    ip_address = models.GenericIPAddressField("IP Address", unique=True)
    agent_id = models.CharField("Agent ID", max_length=100, unique=True)
    last_seen = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "%s (%s)" % (self.agent_id, self.ip_address)

