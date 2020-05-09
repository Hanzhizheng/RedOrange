from rest_framework import (
    viewsets,
    exceptions,
)

from . import (
    models,
    serializers,
    permissions,
)


class PartyAViewSet(viewsets.ModelViewSet):
    queryset = models.PartyA.objects.all()
    serializer_class = serializers.PartyASerializer
    search_fields = ('name',)


class PhotoAlbumViewSet(viewsets.ModelViewSet):
    queryset = models.PhotoAlbum.objects.all()
    serializer_class = serializers.PhotoAlbumSerializer
    filterset_fields = ('party_a',)
    permission_classes = [permissions.PhotoAlbumPermission]


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = models.Campaign.objects.all()
    serializer_class = serializers.CampaignSerializer
    filterset_fields = ('party_a',)
    permission_classes = [permissions.CampaignPermission]
