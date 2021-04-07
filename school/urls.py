from os import listdir
from os.path import join, isdir

from django.conf.urls import include, url
from django.urls import path
from config.settings import BASE_DIR
from rest_framework_swagger.views import get_swagger_view

SCHOOL_API_DIR = 'school/api/'

entities = [directory
            for directory in listdir(join(BASE_DIR, SCHOOL_API_DIR))
            if (isdir(join(BASE_DIR, SCHOOL_API_DIR, directory))
                and directory != '__pycache__')]

urlpatterns = [
    url(r'^', include('school.api.{}.urls'.format(entity)))
    for entity in entities
]
