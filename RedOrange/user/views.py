from rest_framework import (
    viewsets,
    mixins,
    exceptions,
)
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from drf_yasg.utils import (
    swagger_auto_schema,
    no_body,
)

from . import (
    models,
    serializers,
    schemas,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class JobCardViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.JobCard.objects.all()
    serializer_class = serializers.JobCardSerializer
    filterset_fields = ('is_verified', 'party_a',)

    def get_queryset(self):
        action = self.action
        user = self.request.user
        if action == 'list':
            self.queryset = self.queryset.filter(user=user)
        elif action == 'partya_list':
            self.queryset = self.queryset.filter(
                user=user, is_verified=True,
            )
        return super().get_queryset()

    def get_serializer_class(self):
        action = self.action
        if action == 'card_list':
            return serializers.CardListSerializer
        elif action == 'create':
            return serializers.JobCardCreateSerializer
        return self.serializer_class

    @action(methods=['get'], detail=False)
    def partya_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()). \
            values('party_a', 'party_a__name')
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(page)

    def check_perm(self, party_a):
        user = self.request.user
        kwargs = {
            'user': user, 
            'is_verified': True,
            'is_admin': True,
            'party_a': party_a,
        }
        if not self.queryset.filter(**kwargs).exists():
            raise exceptions.PermissionDenied

    @swagger_auto_schema(
        query_serializer=None,
        responses={'200': serializers.CardListSerializer(many=True)},
    )
    @action(methods=['get'], detail=False)
    def card_list(self, request, *args, **kwargs):
        party_a = self.request.query_params['party_a']
        self.check_perm(party_a)
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=no_body,
        responses={'200': '修改成功'},
    )
    @action(methods=['patch'], detail=True)
    def verify(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        self.check_perm(instance.party_a)
        instance.is_verified = True
        instance.save()
        return Response('修改成功')

    @swagger_auto_schema(
        request_body=schemas.PatchAdminReq,
        responses={'200': '修改成功'},
    )
    @action(methods=['patch'], detail=True)
    def admin(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        self.check_perm(instance.party_a)
        get = self.request.data.get
        is_admin = get('is_admin', instance.is_admin)
        position = get('position', instance.position)
        instance.is_admin = is_admin
        instance.position = position
        return Response('修改成功')

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    
    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            self.check_perm(instance.party_a)
        instance.delete()