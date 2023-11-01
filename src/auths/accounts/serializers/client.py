from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from auths.accounts.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'phone', 'full_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        try:
            password_validation.validate_password(value, self.instance)
        except serializers.ValidationError as error:
            self.add_error('password', error)
        return value


class VerifyOTPCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=4)

    def save(self, validated_data):
        refresh = RefreshToken.for_user(validated_data)
        return ({
            'user_id': validated_data.id,
            'success': True,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })