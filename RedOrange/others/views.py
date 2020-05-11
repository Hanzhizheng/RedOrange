from rest_framework import viewsets

from . import models
from . import serializers


class ProvinceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializer
    search_fields = ('name',)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    search_fields = ('name',)
    filterset_fields = ('province',)


class AreaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer
    search_fields = ('name',)
    filterset_fields = ('city',)


class JobCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.JobCategory.objects.all()
    serializer_class = serializers.JobCategorySerializer
    search_fields = ('name',)


class JobSubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.JobSubCategory.objects.all()
    serializer_class = serializers.JobSubCategorySerializer
    search_fields = ('name',)
    filterset_fields = ('category',)