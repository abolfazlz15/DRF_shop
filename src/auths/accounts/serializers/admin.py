from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _


class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:

            user = authenticate(**attrs)

            if not user or not user.is_superuser:
                raise serializers.ValidationError(
                    {'message': _('Unable to log in with provided credentials'), 'success': False})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        return user

    def save(self, validated_data):
        refresh = RefreshToken.for_user(validated_data)
        return ({
            'user_id': validated_data.id,
            'success': True,
            'refresh': str(refresh),
            'access': str(refresh.access_token),

        })
