from rest_framework import serializers
from users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['email', 'password', 'telegram']
