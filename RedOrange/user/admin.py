from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nickname',
        'username',
        'phone',
    )
    search_fields = (
        'username',
        'phone'
    )


class JobCardAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'position',
        'party_a',
        'is_admin',
        'is_verified',
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.JobCard, JobCardAdmin)