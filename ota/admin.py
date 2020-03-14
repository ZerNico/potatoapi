from django.contrib import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

from . import models


class BuildAdmin(admin.ModelAdmin):
    list_display = [
        'filename', 'device', 'dish', 'build_date', 'build_type', 'version',
        'user'
    ]
    search_fields = [
        'filename', 'device', 'dish', 'build_date', 'build_type', 'version',
    ]


class NoteAdmin(admin.ModelAdmin):
    list_display = [
        'device', 'text'
    ]
    search_fields = [
        'device',
    ]


class ChangelogAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = [
        'version', 'android_version', 'date', 'user'
    ]
    search_fields = [
        'version', 'android_version', 'date'
    ]
    list_filter = ['date', ]


admin.site.register(models.Build, BuildAdmin)
admin.site.register(models.Note, NoteAdmin)
admin.site.register(models.Changelog, ChangelogAdmin)
