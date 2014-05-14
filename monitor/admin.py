from django.contrib import admin
from monitor import models


class DispatcherAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)


class ProviderAgentAdmin(admin.ModelAdmin):
    list_display = ('agent_id', 'ip_address')


class DispatcherActionAdmin(admin.ModelAdmin):
    list_display = ('dispatcher', 'name', 'last_run')


admin.site.register(models.Dispatcher, DispatcherAdmin)
admin.site.register(models.ProviderAgent, ProviderAgentAdmin)
admin.site.register(models.DispatcherAction, DispatcherActionAdmin)


