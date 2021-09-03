from django.shortcuts import render
from user.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from config import settings
from .models import Translator, TranslatorSubject
from .serializer import TranslatorSerializer, TranslatorSubjectSerializer


@api_view(['POST'])
@login_required
def apply_translator(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    about_me = request.data.get('about_me')
    hourly_rate = request.data.get('hourly_rate')
    translate_lang = request.data.get('translate_lang')
    translate_lang_len = len(translate_lang)

    translator = Translator.objects.filter(user=user).first()
    if translator is not None:
        translator.about_me = about_me
        translator.hourly_rate = hourly_rate
        translator.save()
    else:
        translator = Translator(user=user, about_me=about_me,
                                hourly_rate=hourly_rate)
        translator.save()
    TranslatorSubject.objects.filter(translator=translator).delete()
    for item in translate_lang:
        subject = item['lang_from']['lang']
        target = item['lang_to']['lang']
        translatorSubject = TranslatorSubject(
            translator=translator, subject=subject, target=target)
        translatorSubject.save()
    translatorSerializer = TranslatorSerializer(translator)
    return Response(data=translatorSerializer.data, status=201)


@api_view(['POST'])
@login_required
def get_translator(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()

    translator = Translator.objects.filter(user=user).first()
    translator_object = {}
    if translator is not None:
        translator_object['about_me'] = translator.about_me
        translator_object['hourly_rate'] = translator.hourly_rate
        translator_object['translate_lang'] = []
        translatorSubjects = TranslatorSubject.objects.filter(
            translator=translator)
        for item in translatorSubjects:
            subject = item.subject
            target = item.target
            translator_object['translate_lang'].append(
                {'lang_from': {'lang': subject}, 'lang_to': {'lang': target}})
        return Response(data=translator_object, status=200)
    else:
        return Response(data=translator_object, status=404)
