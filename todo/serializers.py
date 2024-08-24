from rest_framework import serializers
from .models import TodoModels, RegistationModel, LoginModel
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModels
        fields = '__all__'

    def create(self, validate_data):
        return TodoModels.objects.create(**validate_data)

class RegistationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = '__all__'

    def create(self, validate_data):
        return LoginModel.objects.create(**validate_data)
