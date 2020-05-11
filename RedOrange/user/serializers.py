from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        read_only_fields = (
            'juices',
        )
        fields = (
            'name',
            'nickname',
            'phone',
            'avator',
            'email',
            'brithday',
            'sex',
        )


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


class GiveJuiceSerializer(serializers.Serializer):
    num = serializers.IntegerField(
        required=True,
        min_value=10,
        max_value=100,
        help_text='橙汁数',
    )

    def validate_num(self, value):
        juices = self.context['request'].user.juices
        if juices < value:
            raise serializers.ValidationError('橙汁不足哇')
        return value