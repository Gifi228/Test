from django.contrib import admin

from .models import *


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'file_type']
    search_fields = ['file_type']
    list_filter = ['file_type']


@admin.register(MediaSettings)
class MediaSettingsAdmin(admin.ModelAdmin):
    list_display = ['id']
