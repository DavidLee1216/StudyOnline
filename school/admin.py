from django.contrib import admin
from school.api.teacher.models import Teacher, TeacherSubject, Lecture
from school.api.subject.models import Subject
from .admin_models import TeacherAdmin, TeacherSubjectAdmin, LectureAdmin, SubjectAdmin

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(TeacherSubject, TeacherSubjectAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Subject, SubjectAdmin)
