from . import views
from django.urls import path

urlpatterns = [
    path('teacher/', views.teacher, name='teacher'),
]
