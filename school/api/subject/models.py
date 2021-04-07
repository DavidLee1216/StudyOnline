from django.db import models
from rest_framework import serializers

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    
    def __str__(self):
        return '{}'.format(self.subject_name)
