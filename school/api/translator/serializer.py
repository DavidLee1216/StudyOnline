from django.db import models
from rest_framework import serializers
from .models import Translator, TranslatorSubject


class TranslatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translator
        fields = '__all__'


class TranslatorSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatorSubject
        fields = '__all__'
