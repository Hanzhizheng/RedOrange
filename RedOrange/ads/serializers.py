from rest_framework import serializers

from . import models


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