from rest_framework import serializers

from . import models


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Province
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Area
        fields = '__all__'


class JobCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JobSubCategory
        fields = '__all__'


class JobSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JobSubCategory
        fields = '__all__'