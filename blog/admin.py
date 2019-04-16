from django.contrib import admin

from blog import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    search_fields = ['title', ]


admin.site.register(models.Post, PostAdmin)
