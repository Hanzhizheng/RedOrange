from rest_framework import serializers

from common.serializers import ReadOnlyPartyAMeta
from . import models


class FullTimeJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FullTimeJob
        fields = '__all__'


class PartTimeJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PartTimeJob
        fields = '__all__'


class FullTimeJobUpdateSerializer(serializers.ModelSerializer):

    class Meta(ReadOnlyPartyAMeta):
        model = models.FullTimeJob


class PartTimeJobUpdateSerializer(serializers.ModelSerializer):

    class Meta(ReadOnlyPartyAMeta):
        model = models.PartTimeJob


class PersonalJobSerializer(serializers.ModelSerializer):

    class Meta():
        model = models.PartTimeJob
        read_only_fields = (
            'party_a',
        )
        fields = '__all__'