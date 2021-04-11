from django.shortcuts import render
from user.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from config import settings
from .models import Teacher, TeacherSubject, Lecture
from .serializer import TeacherSerializer, TeacherSubjectSerializer


@api_view(['POST'])
@login_required
def apply_teacher(request):
    email = request.data.get('email')
    user = User.objects.filter(email=email).first()
    about_me = request.data.get('about_me')
    hourly_rate = request.data.get('hourly_rate')
    teach_lang = request.data.get('teach_lang')
    teach_lang_len = len(teach_lang)

    teacher = Teacher.objects.filter(user=user).first()
    if teacher is not None:
        teacher.about_me = about_me
        teacher.hourly_rate = hourly_rate
        teacher.save()
    else:
        teacher = Teacher(user=user, about_me=about_me,
                          hourly_rate=hourly_rate)
        teacher.save()
    TeacherSubject.objects.filter(teacher=teacher).delete()
    for item in teach_lang:
        subject = item['explain_lang']['lang']
        target = item['target_lang']['lang']
        teacherSubject = TeacherSubject(
            teacher=teacher, subject=subject, target=target)
        teacherSubject.save()
    teacherSerializer = TeacherSerializer(teacher)
    return Response(data=teacherSerializer.data, status=201)
