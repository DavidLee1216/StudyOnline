from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from school.api.payment.models import Payment
from user.models import User
from school.api.subject.models import Subject


class Translator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=1000, blank=True)
    hourly_rate = models.DecimalField(
        max_digits=5, decimal_places=2, blank=False)

    def __str__(self):
        return '[{}] {}'.format(self.user, self.title, self.about_me, hourly_rate)


class TranslatorSubject(models.Model):
    translator = models.OneToOneField(Translator, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=False, default="")
    target = models.CharField(max_length=50, blank=False, default="")

    def __str__(self):
        return '[{}] {}'.format(self.teacher, self.subject, self.target)
