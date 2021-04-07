from django.shortcuts import render
from user.models import User
from .models import Profile
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from config import settings
from .serializer import ProfileSerializer
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from django.core.files.storage import FileSystemStorage
import json
from types import SimpleNamespace


@api_view(['POST', 'PUT'])
@login_required
def set_profile(request):  # set profile using function
    if request.method == 'POST':
        email = request.data.get('email')
        country = request.data.get('country')
        city = request.data.get('city')
        photo_url = request.data.get('photo_url')
        birthday = request.data.get('birthday')
        sex = request.data.get('sex')
        interest = request.data.get('interest')
        about_me = request.data.get('about_me')
        native_lang = request.data.get('native_lang')
        study_lang = request.data.get('study_lang')

        native_lang_len = len(native_lang)
        if native_lang_len == 1:
            native_lang.append({'lang': ''})
        study_lang_len = len(study_lang)
        for i in range(study_lang_len, 3):
            study_lang.append({'lang': '', 'level': ''})

        print(request.data)

        user = User.objects.filter(email=email).first()
        if user is not None:
            profiles = Profile.objects.filter(user_id=user)
            if len(profiles) > 0:
                profile = profiles[0]
                profile.user_country = country
                profile.user_city = city
                profile.user_birthday = birthday
                profile.user_sex = sex
                profile.user_photo_url = photo_url
                profile.user_interest = interest
                profile.user_about_me = about_me
                profile.user_native_lang1 = native_lang[0]['lang']
                profile.user_native_lang2 = native_lang[1]['lang']
                profile.user_study_lang1 = study_lang[0]['lang']
                profile.user_study_lang_level1 = study_lang[0]['level']
                profile.user_study_lang2 = study_lang[1]['lang']
                profile.user_study_lang_level2 = study_lang[1]['level']
                profile.user_study_lang3 = study_lang[2]['lang']
                profile.user_study_lang_level3 = study_lang[2]['level']
            else:
                profile = Profile(user_id=user, user_country=country, user_city=city, user_birthday=birthday, user_sex=sex, user_photo_url=photo_url, user_interest=interest,
                                  user_about_me=about_me, user_native_lang1=native_lang[
                                      0]['lang'], user_native_lang2=native_lang[1]['lang'], user_study_lang1=study_lang[0]['lang'],
                                  user_study_lang_level1=study_lang[0]['level'], user_study_lang2=study_lang[
                                      1]['lang'], user_study_lang_level2=study_lang[1]['level'],
                                  user_study_lang3=study_lang[2]['lang'], user_study_lang_level3=study_lang[2]['level'])
            profile.save()

            return Response('success', status=201)
        else:
            return Response('failed', status=404)
    else:
        return Response('success', status=200)


class ProfileViewSet(viewsets.ModelViewSet):  # set profile using viewset
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @login_required
    def post(request):
        email = request.data['email']
        country = request.data['country']
        city = request.data['city']
        photo_url = request.data['photo_url']
        birthday = request.data['birthday']
        sex = request.data['sex']
        interest = request.data['interest']
        about_me = request.data['about_me']
        native_lang = json.load(request.data['native_lang'])
        study_lang = json.load(request.data['study_lang'])
        print('native lang' + ': ' + native_lang)
        print('study lang' + ': ' + study_lang)
        native_lang_len = len(native_lang)
        if native_lang_len == 1:
            native_lang.append({'lang': ''})
        study_lang_len = len(study_lang)
        for i in range(study_lang_len, 3):
            study_lang.append({'lang': '', 'level': ''})

        user = User.objects.filter(email=email).first()
        if user is not None:
            profiles = Profile.objects.filter(user_id=user)
            if len(profiles) > 0:
                profile = profiles[0]
                profile.user_country = country
                profile.user_city = city
                profile.user_birthday = birthday
                profile.user_sex = sex
                profile.user_photo_url = photo_url
                profile.user_interest = interest
                profile.user_about_me = about_me
                profile.user_native_lang1 = native_lang[0]['lang']
                profile.user_native_lang2 = native_lang[1]['lang']
                profile.user_study_lang1 = study_lang[0]['lang']
                profile.user_study_lang_level1 = study_lang[0]['level']
                profile.user_study_lang2 = study_lang[1]['lang']
                profile.user_study_lang_level2 = study_lang[1]['level']
                profile.user_study_lang3 = study_lang[2]['lang']
                profile.user_study_lang_level3 = study_lang[2]['level']
            else:
                profile = Profile(user_id=user, user_country=country, user_city=city, user_birthday=birthday, user_sex=sex, user_photo_url=photo_url, user_interest=interest,
                                  user_about_me=about_me, user_native_lang1=native_lang[
                                      0]['lang'], user_native_lang2=native_lang[1]['lang'], user_study_lang1=study_lang[0]['lang'],
                                  user_study_lang_level1=study_lang[0]['level'], user_study_lang2=study_lang[
                                      1]['lang'], user_study_lang_level2=study_lang[1]['level'],
                                  user_study_lang3=study_lang[2]['lang'], user_study_lang_level3=study_lang[2]['level'])
            profile.save()

            return Response('success', status=201)
        else:
            return Response('failed', status=404)


class ProfileView(APIView):  # set_profile using apiview class
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        email = request.data['email']
        country = request.data['country']
        city = request.data['city']
        photo_url = request.data['photo_url'] if 'photo_url' in request.data else ""
        birthday = request.data['birthday']
        sex = request.data['sex']
        interest = request.data['interest']
        about_me = request.data['about_me']
        native_lang = json.loads(
            request.data['native_lang'])
        study_lang = json.loads(
            request.data['study_lang'])
        native_lang_len = len(native_lang)
        if native_lang_len == 1:
            native_lang.append({'lang': ''})
        study_lang_len = len(study_lang)
        for i in range(study_lang_len, 3):
            study_lang.append({'lang': '', 'level': ''})
        user = User.objects.filter(email=email).first()
        profiles = Profile.objects.filter(user_id=user)
        if len(profiles) > 0:
            profile = profiles[0]
            profile.user_country = request.data['country']
            profile.user_city = request.data['city']
            profile.user_birthday = request.data['birthday']
            profile.user_sex = request.data['sex']
            if 'photo_url' in request.data:
                profile.user_photo_url = request.data['photo_url']
            profile.user_interest = request.data['interest']
            profile.user_about_me = request.data['about_me']
            profile.user_native_lang1 = native_lang[0]['lang']
            profile.user_native_lang2 = native_lang[1]['lang']
            profile.user_study_lang1 = study_lang[0]['lang']
            profile.user_study_lang_level1 = study_lang[0]['level']
            profile.user_study_lang2 = study_lang[1]['lang']
            profile.user_study_lang_level2 = study_lang[1]['level']
            profile.user_study_lang3 = study_lang[2]['lang']
            profile.user_study_lang_level3 = study_lang[2]['level']
            profile.save()
            profileSerializer = ProfileSerializer(profile)
            return Response(data=profileSerializer.data, status=200)
        else:
            profile = Profile(user_id=user, user_country=country, user_city=city, user_birthday=birthday, user_sex=sex, user_photo_url=photo_url, user_interest=interest,
                              user_about_me=about_me, user_native_lang1=native_lang[
                                  0]['lang'], user_native_lang2=native_lang[1]['lang'], user_study_lang1=study_lang[0]['lang'],
                              user_study_lang_level1=study_lang[0]['level'], user_study_lang2=study_lang[
                                  1]['lang'], user_study_lang_level2=study_lang[1]['level'],
                              user_study_lang3=study_lang[2]['lang'], user_study_lang_level3=study_lang[2]['level'])
            profile.save()
            profileSerializer = ProfileSerializer(profile)
            # profileSerializer.save()
            return Response(data=profileSerializer.data, status=201)


@api_view(['POST'])
@ login_required
def get_profile(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    profiles = Profile.objects.filter(user_id=user)
    if len(profiles) > 0:
        profile = profiles[0]
        profile_serialized = ProfileSerializer(profile)
        return Response(profile_serialized.data, status=200)
    return Response('failed', status=404)


# @api_view(['POST'])
# @login_required
# def upload_profile_photo(request):
#     print(request.data)
#     if request.method == 'POST' and request.FILES['file']:
#         photofile = request.FILES['file']
#         fs = FileSystemStorage()
#         filename = fs.save(photofile.name, photofile)
#         uploaded_file_url = fs.url(filename)
#         return Response(data=uploaded_file_url, status=200)


# class UploadProfilePhotoView(APIView):
#     parser_class = (FileUploadParser,)

#     def post(self, request, format=None):
#         print(request.data)
#         if 'file' not in request.data:
#             raise ParseError("Empty content")

#         photofile = request.data['file']
#         print(photofile)
#         fs = FileSystemStorage()
#         filename = fs.save(photofile.name, photofile)
#         uploaded_file_url = fs.url(filename)
#         return Response(data=uploaded_file_url, status=201)
