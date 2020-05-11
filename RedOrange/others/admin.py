from django.contrib import admin

from . import models


class CommonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
    )
    search_fields = (
        'name',
    )


class ProvinceAdmin(CommonAdmin):
    pass


class CityAdmin(CommonAdmin):
    list_display = (
        'name',
        'code',
        'province',
    )
    list_filter = (
        'province',
    )


class AreaAdmin(CommonAdmin):
    list_display = (
        'name',
        'code',
        'city',
    )
    list_filter = (
        'city',
    )


class JobCategoryAdmin(CommonAdmin):
    pass


class JobSubCategoryAdmin(CommonAdmin):
    list_display = (
        'name',
        'code',
        'category',
    )
    list_filter = (
        'category',
    )


admin.site.register(models.Province, ProvinceAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Area, AreaAdmin)
admin.site.register(models.JobCategory, JobCategoryAdmin)
admin.site.register(models.JobSubCategory, JobSubCategoryAdmin)