from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'phone',
    )
    search_fields = (
        'username',
        'phone'
    )


admin.site.register(models.User, UserAdmin)