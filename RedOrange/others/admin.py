from django.contrib import admin

from . import models


class ProvinceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
    )
    search_fields = (
        'name',
    )


class CityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'province',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'province',
    )


class AreaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'city',
    )
    search_fields = (
        'name',
        'city',
    )
    list_filter = (
        'city',
    )


admin.site.register(models.Province, ProvinceAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Area, AreaAdmin)