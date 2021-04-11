from django.contrib import admin
from school.api.teacher.models import Teacher, TeacherSubject, Lecture
from school.api.translator.models import Translator, TranslatorSubject
from school.api.subject.models import Subject
from .admin_models import TeacherAdmin, TeacherSubjectAdmin, TranslatorAdmin, TranslatorSubjectAdmin, LectureAdmin, SubjectAdmin

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubject, TeacherSubjectAdmin)
admin.site.register(Translator, TranslatorAdmin)
admin.site.register(TranslatorSubject, TranslatorSubjectAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subject, SubjectAdmin)
