from django.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework import serializers
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from school.api.payment.models import Payment
from user.models import User
from school.api.subject.models import Subject


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about_me = models.TextField(max_length=1000, blank=True)
    hourly_rate = models.DecimalField(
        max_digits=5, decimal_places=2, blank=False)

    def __str__(self):
        return '[{}] {}'.format(self.user, self.title, self.about_me, hourly_rate)


def upload_path(instance, filename):
    return ('/'.join(['lectures', str(instance.teacher_id), filename]))


class TeacherSubject(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    explain = models.CharField(max_length=50, blank=False, default="")
    target = models.CharField(max_length=50, blank=False, default="")

    def __str__(self):
        return '[{}] {}'.format(self.teacher, self.subject, self.target)


class Lecture(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(
        to=TeacherSubject, null=True, on_delete=models.CASCADE)
    ref_file = models.FileField(
        _('file url'), blank=True, null=True, upload_to=upload_path)
    upload_date = models.DateField(
        _('date uploaded'), blank=False, default=timezone.now)

    def __str__(self):
        return '[{}] {}'.format(self.teacher, self.subject, self.ref_file, self.upload_date)
