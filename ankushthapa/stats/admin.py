from django.contrib import admin
from stats.models import AccessLogs

class StatsAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'access_string']
    list_filter = ['page_name']
admin.site.register(AccessLogs, StatsAdmin)
