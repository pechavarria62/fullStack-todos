from rest_framework import serializers
from .models import CustomUser

# Serializer to handle user creation
class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        # Create user using Django's built-in method
        user = CustomUser.objects.create_user(**validated_data)
        return user