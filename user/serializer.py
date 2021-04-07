from django.db import models
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'last_login', 'date_joined', 'is_superuser']
