from django.contrib import admin

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


admin.site.register(models.Build, BuildAdmin)
admin.site.register(models.Note, NoteAdmin)
