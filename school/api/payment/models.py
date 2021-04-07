from django.db import models
from user.models import User
from rest_framework import serializers

class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creditcard = models.CharField(max_length=200)
    paypal = models.CharField(max_length=200)
    
    def __str__(self):
        return '{}'.format(user_id)