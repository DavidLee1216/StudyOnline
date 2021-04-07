from django.db import models
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user_country', 'user_city', 'user_birthday', 'user_sex', 'user_photo_url', 'user_interest', 'user_about_me',
                  'user_native_lang1', 'user_native_lang2', 'user_study_lang1', 'user_study_lang_level1', 'user_study_lang2', 'user_study_lang_level2',
                  'user_study_lang3', 'user_study_lang_level3']
