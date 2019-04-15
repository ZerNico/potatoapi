from django.contrib import admin

from user import models


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'is_staff', 'email', 'date_joined', 'country', 'device'
    ]
    list_filter = ['is_staff', 'date_joined']
    search_fields = ['username', 'email', 'country', 'device']


admin.site.register(models.User, UserAdmin)
