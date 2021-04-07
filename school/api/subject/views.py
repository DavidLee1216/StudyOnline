from django.shortcuts import render
from user.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from config import settings


@api_view(['GET', 'POST', 'PUT'])
@login_required
def subject():
    pass
