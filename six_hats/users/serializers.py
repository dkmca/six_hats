from rest_framework import serializers

from users.models import User


class AddUserSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=False)
    email = serializers.CharField(allow_blank=False)
    address = serializers.CharField(allow_blank=False)


class UpdateUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(allow_null=False)
    name = serializers.CharField(allow_blank=False)
    email = serializers.CharField(allow_blank=False)
    address = serializers.CharField(allow_blank=False)


class DeleteUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'address']