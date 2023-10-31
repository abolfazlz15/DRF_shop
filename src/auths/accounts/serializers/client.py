from django.contrib.auth import password_validation
from rest_framework import serializers

from auths.accounts.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        try:
            password_validation.validate_password(value, self.instance)
        except serializers.ValidationError as error:
            self.add_error('password', error)
        return value
