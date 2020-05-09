from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'


class JobCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JobCard
        fields = '__all__'


class CardListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(
        source='user.name',
        help_text='用户姓名',
    )

    class Meta:
        model = models.JobCard
        read_only_fields = (
            'id',
            'user_name',
            'position',
            'is_admin',
        )
        fields = read_only_fields


class JobCardCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.JobCard
        fields = (
            'position',
            'party_a',
        )
