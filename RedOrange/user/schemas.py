from rest_framework import serializers

from . import models


class PatchAdminReq(serializers.Serializer):
    is_admin = serializers.BooleanField(
        required=False,
        help_text='是否是管理员',
    )
    position = serializers.CharField(
        required=False,
        help_text='岗位',
    )