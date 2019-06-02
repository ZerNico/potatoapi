from django.contrib import admin

from . import models


class BuildAdmin(admin.ModelAdmin):
    list_display = [
        'filename', 'device', 'build_date', 'build_type', 'version', 'private',
        'user'
    ]
    search_fields = [
        'filename', 'device', 'build_date', 'build_type', 'version', 'private',
    ]


admin.site.register(models.Build, BuildAdmin)
