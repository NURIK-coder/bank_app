from rest_framework import serializers

from users.models import User


class UserSerialize(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'phone', 'password', 'avatar']

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'phone', 'avatar']

