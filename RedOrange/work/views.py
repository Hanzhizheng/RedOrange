from rest_framework import (
    viewsets,
)

from . import (
    models,
    serializers,
    permissions,
)


class FullTimeJobViewSet(viewsets.ModelViewSet):
    queryset = models.FullTimeJob.objects.all()
    serializer_class = serializers.FullTimeJobSerializer
    filterset_fields = ('party_a', 'category', 'sub_category')
    permission_classes = [permissions.FullTimeJobPermission]

    def get_serializer_class(self):
        action = self.action
        if action == 'partial_update':
            return serializers.FullTimeJobUpdateSerializer
        return self.serializer_class


class PartTimeJobViewSet(viewsets.ModelViewSet):
    queryset = models.PartTimeJob.objects.all()
    serializer_class = serializers.PartTimeJobSerializer
    filterset_fields = ('party_a', 'category', 'sub_category')
    permission_classes = [permissions.PartTimeJobPermission]

    def get_serializer_class(self):
        action = self.action
        if action == 'partial_update':
            return serializers.PartTimeJobUpdateSerializer
        return self.serializer_class


class PersonalJobViewSet(viewsets.ModelViewSet):
    queryset = models.PersonalJob.objects.all()
    serializer_class = serializers.PersonalJobSerializer
    filterset_fields = ('user', 'category', 'sub_category')