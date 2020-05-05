from django.contrib import admin

from . import models


class PartyAAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'boss',
    )
    search_fields = (
        'name',
    )


class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = (
        'img',
        'party_a',
    )
    list_filter = (
        'party_a',
    )


class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'start_date',
        'stop_date',
        'party_a',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'party_a',
    )


admin.site.register(models.PartyA, PartyAAdmin)
admin.site.register(models.PhotoAlbum, PhotoAlbumAdmin)
admin.site.register(models.Campaign, CampaignAdmin)