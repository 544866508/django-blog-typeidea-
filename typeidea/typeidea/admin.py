from django.contrib.admin.models import LogEntry
from django.contrib import admin


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']