from django.db import models
from user.models import User
from rest_framework import serializers


def upload_path(instance, filename):
    return ('/'.join(['profiles', str(instance.user_id_id), filename]))


class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_country = models.CharField(max_length=200, blank=False)
    user_city = models.CharField(max_length=200, blank=False)
    user_birthday = models.DateField(blank=False)
    user_sex = models.CharField(max_length=20, blank=False)
    user_photo_url = models.ImageField(
        blank=True, null=True, upload_to=upload_path)
    user_interest = models.CharField(max_length=200, blank=True)
    user_about_me = models.TextField(max_length=2000, blank=True)
    user_native_lang1 = models.CharField(max_length=50, blank=True)
    user_native_lang2 = models.CharField(max_length=50, blank=True)
    user_study_lang1 = models.CharField(max_length=50, blank=True)
    user_study_lang_level1 = models.CharField(max_length=50, blank=True)
    user_study_lang2 = models.CharField(max_length=50, blank=True)
    user_study_lang_level2 = models.CharField(max_length=50, blank=True)
    user_study_lang3 = models.CharField(max_length=50, blank=True)
    user_study_lang_level3 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '[{}] {}, {}'.format(self.user_id, self.user_country, self.user_city, self.user_birthday, self.user_sex, self.user_photo_url, self.user_interest, self.user_about_me, self.user_native_lang1, self.user_native_lang2, self.user_study_lang1, self.user_study_lang2, self.user_study_lang3)
