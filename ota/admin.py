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


admin.site.register(models.Build, BuildAdmin)
