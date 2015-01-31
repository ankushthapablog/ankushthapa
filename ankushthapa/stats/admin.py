from django.contrib import admin
from stats.models import AccessLogs


class StatsAdmin(admin.ModelAdmin):
    pass
admin.site.register(AccessLogs, StatsAdmin)
