from rest_framework import serializers

from . import models
from common.serializers import ReadOnlyPartyAMeta


class PartyASerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PartyA
        fields = '__all__'


class PhotoAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PhotoAlbum
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Campaign
        fields = '__all__'


class PhotoAlbumUpdateSerializer(serializers.ModelSerializer):

    class Meta(ReadOnlyPartyAMeta):
        model = models.PhotoAlbum


class CampaignUpdateSerializer(serializers.ModelSerializer):

    class Meta(ReadOnlyPartyAMeta):
        model = models.Campaign