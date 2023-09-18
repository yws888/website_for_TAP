from django.contrib import admin

from .models import Item

from django.contrib.admin.models import LogEntry

from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

admin.site.register(Item)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'

    # to filter the results by users, and action flags { 1:'Add',2:'Change',3:'Delete'}
    # list_filter = [
    #     'user',
    #     'action_flag'
    # ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'object_repr',
        'action_flag',
        '__str__',
        #'change_message',
        'object_id'
    ]